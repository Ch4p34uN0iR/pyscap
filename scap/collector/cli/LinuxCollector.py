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

from scap.collector.CLICollector import CLICollector
import logging

logger = logging.getLogger(__name__)
class LinuxCollector(CLICollector):
    def collect(self):
        from scap.collector.cli.linux.SystemUUIDCollector import SystemUUIDCollector
        SystemUUIDCollector(self.host, self.args).collect()

        from scap.collector.cli.linux.CPECollector import CPECollector
        CPECollector(self.host, self.args).collect()

        from scap.collector.cli.linux.HostnameCollector import HostnameCollector
        HostnameCollector(self.host, self.args).collect()

        from scap.collector.cli.linux.FQDNCollector import FQDNCollector
        FQDNCollector(self.host, self.args).collect()

        from scap.collector.cli.linux.NetworkConnectionCollector import NetworkConnectionCollector
        NetworkConnectionCollector(self.host, self.args).collect()

        from scap.collector.cli.linux.NetworkServiceCollector import NetworkServiceCollector
        NetworkServiceCollector(self.host, self.args).collect()

        from scap.collector.cli.linux.IdentityCollector import IdentityCollector
        IdentityCollector(self.host, self.args).collect()
