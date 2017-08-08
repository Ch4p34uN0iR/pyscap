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
import pprint

from scap.Collector import Collector
from scap.model.cpe_matching_2_3.CPE import CPE

logger = logging.getLogger(__name__)
class LshwCollector(Collector):
    def collect(self):
        if 'lshw' in self.host.facts:
            return

        # TODO convert to a provider collector
        try:
            path = [{}]
            indents = [0]
            return_code, out_lines, err_lines = self.host.exec_command('sudo -S lshw')
            for line in out_lines:
                m = re.match(r'^([ ]+)\*-(\S+)', line)
                if m:
                    if 'vendor' in path[-1] and 'product' in path[-1] and path[-1]['vendor'] != '000000000000':
                        cpe = CPE(part='h', vendor=path[-1]['vendor'], product=path[-1]['product'])
                        if 'version' in path[-1]:
                            cpe.set_value('version', path[-1]['version'])

                        # we don't add duplicates
                        if cpe not in self.host.facts['cpe']['hardware']:
                            self.host.facts['cpe']['hardware'].append(cpe)

                    indent = len(m.group(1))
                    hw_class = m.group(2)
                    cur_indent = indents[-1]
                    if indent > cur_indent:
                        # child; push onto the path
                        path[-1][hw_class] = {}
                        path.append(path[-1][hw_class])
                        indents.append(indent)
                    elif indent == cur_indent:
                        # sibling; pop then push
                        path.pop()
                        indents.pop()
                        path[-1][hw_class] = {}
                        path.append(path[-1][hw_class])
                        indents.append(indent)
                    else:
                        # indent < cur_indent
                        # parent; ascend till the indent is equal
                        parent_indent = indents[-1]
                        while parent_indent >= indent:
                            path.pop()
                            indents.pop()
                            parent_indent = indents[-1]
                        path[-1][hw_class] = {}
                        path.append(path[-1][hw_class])
                        indents.append(indent)
                    continue

                m = re.match(r'^\s+([^:]+): (.*)\s*$', line)
                if m:
                    if m.group(1) == 'configuration':
                        path[-1][m.group(1)] = {}

                        # the below mess is because the values don't escape spaces
                        # so guessing is required
                        keys = []
                        in_key = True
                        (k,v) = ('','')
                        for c in m.group(2):
                            if in_key:
                                if c == '=':
                                    in_key = False
                                elif c == ' ':
                                    # not a key, append to prev value
                                    path[-1][m.group(1)][keys[-1]] += ' ' + k
                                    k = ''
                                else:
                                    k += c
                            else:
                                if c == ' ':
                                    in_key = True
                                    path[-1][m.group(1)][k] = v
                                    keys.append(k)
                                    (k,v) = ('','')
                                else:
                                    v += c
                        path[-1][m.group(1)][k] = v
                    elif m.group(1) == 'capabilities':
                        path[-1][m.group(1)] = m.group(2).split(' ')
                    else:
                        path[-1][m.group(1)] = m.group(2)
        except:
            pass
