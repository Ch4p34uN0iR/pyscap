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

from scap.Model import Model
from scap.model.oval_5 import *
from scap.model.oval_5.defs import *

logger = logging.getLogger(__name__)

class TestType(Model):
    MODEL_MAP = {
        'elements': [
            {'xmlns': 'http://www.w3.org/2000/09/xmldsig#', 'tag_name': 'Signature', 'min': 0, 'max': 1},
            {'xmlns': 'http://oval.mitre.org/XMLSchema/oval-common-5', 'tag_name': 'notes', 'class': 'NotesType', 'min': 0, 'max': 1},
        ],
        'attributes': {
            'id': {'type': 'scap.model.oval_5.TestIdPattern', 'required': True},
            'version': {'type': 'NonNegativeInteger', 'required': True},
            'check_existence': {'enum': EXISTENCE_ENUMERATION, 'default': 'at_least_one_exists'},
            'check': {'enum': CHECK_ENUMERATION, 'required': True},
            'state_operator': {'enum': OPERATOR_ENUMERATION, 'default': 'AND'},
            'comment': {'type': 'scap.model.oval_5.NonEmptyString', 'required': True},
            'deprecated': {'type': 'Boolean', 'default': False},
        },
    }

    def resolve_object(self):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)

    def resolve_states(self):
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
