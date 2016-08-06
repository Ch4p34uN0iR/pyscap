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

logger = logging.getLogger(__name__)
class ObjectType(Model):
    # abstract
    def __init__(self):
        super(ObjectType, self).__init__()

        self.set = None
        self.filter = None

        self.ignore_attributes.extend([
            'version',
            'comment',
        ])
        self.ignore_sub_elements.extend([
            '{http://www.w3.org/2000/09/xmldsig#}Signature',
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}notes',
        ])

    def parse_attribute(self, name, value):
        if name == 'deprecated':
            logger.warning('Using deprecated object ' + self.id)
        else:
            return super(ObjectType, self).parse_attribute(name, value)
        return True

    def parse_element(self, sub_el):
        if sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}set':
            from scap.model.oval_defs_5.Set import Set
            s = Set()
            s.from_xml(self, sub_el)
            self.set = s
        elif sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}filter':
            from scap.model.oval_defs_5.Filter import Filter
            f = Filter()
            f.from_xml(self, sub_el)
            self.filter = f
        else:
            return super(ObjectType, self).parse_element(sub_el)
        return True