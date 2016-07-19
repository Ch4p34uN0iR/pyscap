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

from scap.Model import Model
import logging
from scap.Engine import Engine

logger = logging.getLogger(__name__)
class Criteria(Model):
    def from_xml(self, parent, el):
        super(self.__class__, self).from_xml(parent, el)

        if 'operator' in el.attrib:
            self.operator = el.attrib['operator']
        else:
            self.operator = 'AND'

        if 'negate' in el.attrib and (el.attrib['negate'] == 'true' or el.attrib['negate'] == '1'):
            self.negate = True
        else:
            self.negate = False

        if 'applicability_check' in el.attrib and (el.attrib['applicability_check'] == 'true' or el.attrib['applicability_check'] == '1'):
            self.applicability_check = True
        else:
            self.applicability_check = False

        from scap.model.oval_defs_5.Criterion import Criterion
        from scap.model.oval_defs_5.ExtendDefinition import ExtendDefinition
        self.criteria = []
        for crit_el in el:
            if crit_el.tag.endswith('criteria'):
                c = Criteria()
                c.from_xml(self, crit_el)
                self.criteria.append(c)
            elif crit_el.tag.endswith('criterion'):
                c = Criterion()
                c.from_xml(self, crit_el)
                self.criteria.append(c)
            elif crit_el.tag.endswith('extend_definition'):
                ed = ExtendDefinition()
                ed.from_xml(self, crit_el)
                self.criteria.append(ed)
            else:
                logger.critical('Unknown tag in criteria: ' + crit_el.tag)
                import sys
                sys.exit()