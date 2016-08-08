#!/usr/bin/env python
#
# Copyright 2015 BMC Software, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from unittest import TestCase
from StringIO import StringIO
from datetime import datetime
import sys
from port_scanner import PortScanner


class TestPortScanner(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_constructor(self):
        scanner = PortScanner()

    def test_run(self):
        scanner = PortScanner(host="httpbin.org", port=80, count=1)
        count = scanner.scan_port()
        self.assertEqual(count, 1)

    def test_output_measurement(self):
        my_stdout = StringIO()
        old_stdout = sys.stdout
        sys.stdout = my_stdout

        scanner = PortScanner()
        now = datetime.now()
        scanner.source = "FOO"
        scanner.response = 100
        timestamp = int(datetime.strftime(now, '%s'))
        scanner.timestamp = timestamp
        scanner.output_measurements()
        self.assertEqual("PORT_RESPONSE 100 FOO {0}\n".format(timestamp), my_stdout.getvalue())

        sys.stdout = old_stdout

