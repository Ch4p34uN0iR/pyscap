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
class NtUserStateElement(StateType):
    MODEL_MAP = {
        'xml_namespace': 'http://oval.mitre.org/XMLSchema/oval-definitions-5#windows',
        'tag_name': 'ntuser_state',
        'elements': {
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}key': {'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}name': {'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sid': {'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}username': {'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}account_type': {'class': 'EntityStateNTUserAccountTypeType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}logged_on': {'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}enabled': {'class': 'oval_defs_5.EntityStateBoolType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}date_modified': {'class': 'oval_defs_5.EntityStateIntType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}days_since_modified': {'class': 'oval_defs_5.EntityStateIntType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}filepath': {'class': 'oval_defs_5.EntityStateStringType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}last_write_time': {'class': 'oval_defs_5.EntityStateIntType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}type': {'class': 'oval_defs_5.EntityStateRegistryTypeType', 'min': 0},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}value': {'class': 'oval_defs_5.EntityStateAnySimpleType', 'min': 0},
        },
        'element_order': []
    }
