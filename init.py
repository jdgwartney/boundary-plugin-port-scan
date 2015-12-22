#!/usr/bin/env python
# Copyright 2014 Boundary, Inc.
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
from time import sleep
import socket
from sys import stdout, stderr
import json


class PortScanPlugin:

    def __init__(self):
        self.host = None
        self.port = None
	self.pollInterval = None
	self.source = socket.gethostname()
        self.result = None
        self.response = None
        self.config = None

    def parse_configuration(self):
        with open('param.json') as f:
            self.config = json.load(f)
            self.host = self.config['host']
            self.port = self.config['port']
            self.poll_interval = float(self.config['pollInterval']) / 1000.0
	    if len(self.config['source']) > 0:
	    	self.source = self.config['source']
	    else:
		self.source = self.host

    def total_seconds(self, td):
        return (float(td.microseconds) + (float(td.seconds) + float(td.days) * 24 * 3600) * 10**6) / 10**6

    def print_metric(self):
        # Port is consider available if the connection is successful
        if self.result == 0:
            lresult = 1
        else:
            lresult = 0
        stdout.write("PORT_AVAILABILITY {0} {1}\n".format(lresult, self.source))
        stdout.write("PORT_RESPONSE {0} {1}\n".format(self.response, self.source))
	stdout.flush()

    def execute(self):
        self.parse_configuration()
        self.scan_ports()

    def scan_ports(self):
        while True:
            t1 = datetime.now()
            try:
                ip = socket.gethostbyname(self.host)
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # Returns 0 if successful otherwise errno indicating the error
                self.result = sock.connect_ex((ip, self.port))
                sock.close()
            except socket.gaierror:
                stderr.write("Hostname could not be resolved.\n")
            except socket.error:
                stderr.write("Couldn't connect to server\n")
            # Checking the time again
            t2 = datetime.now()

            # Calculates the difference of time, to see how long it took to run the script
            t = t2 - t1
            self.response = self.total_seconds(t) * 1000
            self.print_metric()
            sleep(self.poll_interval)

if __name__ == "__main__":
    p = PortScanPlugin()
    p.execute()

