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

import socket
import json
from threading import Thread, Lock
from port_scanner import PortScanner


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

    def execute(self):
        self.parse_configuration()
        self.run()

    def run(self):
        stdoutmutex = Lock()  # same as thread.allocate_lock()

        threads = []
        config_items = self.config['items']
        print(len(config_items))
        for item in config_items:
            host = item['host']
            port = item['port']
            source = item['source']
            if len(source) == 0:
                source = host
            interval = item['pollInterval']

            print(host)
            p = PortScanner(host=host,
                            port=port,
                            source=source,
                            interval=interval,
                            mutex=stdoutmutex)
            thread = Thread(target=p.scan_port())
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()  # wait for thread exits

if __name__ == "__main__":
    p = PortScanPlugin()
    p.execute()
