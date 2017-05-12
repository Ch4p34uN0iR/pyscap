# Copyright 2016 Casey Jaymes

# This file is part of PySCAP.
#
# PySCAP is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PySCAP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PySCAP.  If not, see <http://www.gnu.org/licenses/>.

import logging
import re

from scap.collector.cli.linux.Collector import Collector

logger = logging.getLogger(__name__)
class IpAddrCollector(Collector):
    def collect(self):
        if 'network_connections' not in self.host.facts:
            self.host.facts['network_connections'] = {}

        return_code, out_lines, err_lines = self.host.exec_command('ip addr')
        for line in out_lines:
            # index line
            m = re.match(r'^\d+:\s+([A-Za-z0-9.]+):', line)
            if m:
                dev = m.group(1)
                if dev not in self.host.facts['network_connections']:
                    self.host.facts['network_connections'][dev] = {
                        'network_addresses': []
                    }
                continue

            # link line
            m = re.match(r'^\s+link/(ether|loopback) ([:a-f0-9]+)', line)
            if m:
                mac = m.group(2)
                if mac == '00:00:00:00:00:00':
                    continue
                self.host.facts['network_connections'][dev]['mac_address'] = mac
                continue

            # inet line
            m = re.match(r'^\s+inet ([0-9.]+)(/\d+)', line)
            if m:
                if 'network_addresses' not in self.host.facts['network_connections'][dev]:
                    self.host.facts['network_connections'][dev]['network_addresses'] = []
                addr = m.group(1)
                subnet_mask = m.group(2)
                self.host.facts['network_connections'][dev]['network_addresses'].append({
                    'type': 'ipv4',
                    'address': addr,
                    'subnet_mask': subnet_mask,
                })
                continue

            # inet6 line
            m = re.match(r'^\s+inet6 ([0-9:]+)(/\d+)', line)
            if m:
                if 'network_addresses' not in self.host.facts['network_connections'][dev]:
                    self.host.facts['network_connections'][dev]['network_addresses'] = []
                addr = m.group(1)
                subnet_mask = m.group(2)
                self.host.facts['network_connections'][dev]['network_addresses'].append({
                    'type': 'ipv6',
                    'address': addr,
                    'subnet_mask': subnet_mask,
                })
                continue
