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
class oval_definitions(Model):
    def __init__(self):
        super(oval_definitions, self).__init__()    # {http://oval.mitre.org/XMLSchema/oval-definitions-5}oval_definitions

        self.definitions = {}
        self.tests = {}
        self.objects = {}
        self.states = {}
        self.variables = {}

        self.ignore_sub_elements.extend([
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5}generator',
            '{http://www.w3.org/2000/09/xmldsig#}Signature',
        ])

    def parse_sub_el(self, sub_el):
        if sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}definitions':
            for def_el in sub_el:
                self.tests[def_el.attrib['id']] = Model.load_child(self, def_el)
        elif sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}tests':
            for test_el in sub_el:
                self.tests[test_el.attrib['id']] = Model.load_child(self, test_el)
        elif sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}objects':
            for obj_el in sub_el:
                self.objects[obj_el.attrib['id']] = Model.load_child(self, obj_el)
        elif sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}states':
            for state_el in sub_el:
                self.states[state_el.attrib['id']] = Model.load_child(self, state_el)
        elif sub_el.tag == '{http://oval.mitre.org/XMLSchema/oval-definitions-5}variables':
            for var_el in sub_el:
                self.variables[var_el.attrib['id']] = Model.load_child(self, var_el)
        else:
            return super(oval_definitions, self).parse_sub_el(sub_el)
        return True