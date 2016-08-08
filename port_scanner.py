#!/usr/bin/env python
# Copyright 2015 BMC Software, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import datetime
import socket
from time import sleep
import sys
from meterplugin import Collector


class PortScanCollector(Collector):

    def __init__(self, host='localhost', port=80, source='localhost', interval=5000, count=None, mutex=None):
        self.host = host
        self.port = port
        self.source = source
        self.interval = interval
        self.count = count
        self.mutex = mutex
        self.response = None
        self.timestamp = None
        self.result = None

    def total_seconds(self, td):
        return (float(td.microseconds) + (float(td.seconds) + float(td.days) * 24 * 3600) * 10 ** 6) / 10 ** 6

    def send_measurement(self):
        self.measurement.send(metric='PORT_RESPONSE',
                              value=self.response,
                              source=self.source,
                              timestamp=self.timestamp)

    def output_measurements(self):
        """
        Outputs measurements to standard out
        :return: None
        """
        if self.mutex is not None:
            with self.mutex:
                self.send_measurement()
        else:
            self.send_measurement()

    def scan_port(self):
        count = 0
        while True:
            count += 1
            try:
                t1 = datetime.now()
                self.response = None
                ip = socket.gethostbyname(self.host)
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(float(self.interval/1000.0))
                self.result = sock.connect((ip, self.port))
                sock.close()

                # Checking the time again
                t2 = datetime.now()

                # Calculates the difference of time, to see how long it took to run the script
                t = t2 - t1

                self.response = self.total_seconds(t) * 1000

            except socket.gaierror:
                self.result = None
                sys.stderr.write("Hostname could not be resolved.\n")
                sys.stderr.flush()
            except socket.timeout:
                self.result = None
                sys.stderr.write("Socket connection timed out.\n")
                sys.stderr.flush()
            except socket.error:
                self.result = None
                sys.stderr.write("Couldn't connect to server\n")
                sys.stderr.flush()

            now = datetime.now()
            self.timestamp = int(datetime.strftime(now, "%s"))
            if self.result is None:
                self.result = -1
            self.output_measurements()
            if self.count is not None and count >= self.count:
                return self.count
            sleep(self.interval/1000.0)

if __name__ == '__main__':
    portscanner = PortScanner(host="httpbin.org", port=80)
    portscanner.scan_port()
