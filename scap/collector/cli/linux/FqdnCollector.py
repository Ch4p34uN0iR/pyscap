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

from scap.Collector import Collector

logger = logging.getLogger(__name__)
class FqdnCollector(Collector):
    def collect(self):
        self.host.facts['fqdn'] = []
        return_code, out_lines, err_lines = self.host.exec_command('hostname --all-fqdns 2>/dev/null')
        for fqdn in out_lines[0].split(' '):
            if len(fqdn) > 0 and fqdn not in self.host.facts['fqdn']:
                self.host.facts['fqdn'].append(fqdn)

        # we don't want there to be no fqdns at all
        if len(self.host.facts['fqdn']) == 0:
            if 'hostname' not in self.host.facts:
                from scap.collector.cli.linux.HostnameCollector import HostnameCollector
                HostnameCollector(self.host).collect()
            self.host.facts['fqdn'].append(self.host.facts['hostname'])

        for fqdn in self.host.facts['fqdn']:
            logger.debug('FQDN: ' + fqdn)
