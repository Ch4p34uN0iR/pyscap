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

from scap.model.oval_defs_5.StateType import StateType
import logging

logger = logging.getLogger(__name__)
class EnvironmentVariable58StateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'environmentvariable58_state',
        'elements': {
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}pid': {'class': 'oval_defs_5.EntityObjectIntType', 'min': 0, 'max': 1},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}name': {'class': 'oval_defs_5.EntityObjectStringType', 'min': 0, 'max': 1},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}value': {'class': 'oval_defs_5.EntityStateAnySimpleType', 'min': 0, 'max': 1},
        },
    }
