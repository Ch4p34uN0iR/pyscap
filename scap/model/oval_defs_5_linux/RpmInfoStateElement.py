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
class RpmInfoStateElement(StateType):
    MODEL_MAP = {
        'tag_name': 'rpminfo_state',
        'elements': {
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}name': {'class': 'oval_defs_5.EntityStateStringType', 'min': 0, 'max': 1},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}arch': {'class': 'oval_defs_5.EntityStateStringType', 'min': 0, 'max': 1},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}epoch': {'class': 'EpochElement', 'min': 0, 'max': 1},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}release': {'class': 'ReleaseElement', 'min': 0, 'max': 1},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}version': {'class': 'VersionElement', 'min': 0, 'max': 1},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}evr': {'class': 'oval_defs_5.EntityStateEVRStringType', 'min': 0, 'max': 1},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}signature_keyid': {'class': 'oval_defs_5.EntityStateStringType', 'min': 0, 'max': 1},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}extended_name': {'class': 'oval_defs_5.EntityStateStringType', 'min': 0, 'max': 1},
            '{http://oval.mitre.org/XMLSchema/oval-definitions-5#linux}filepath': {'class': 'oval_defs_5.EntityStateStringType', 'min': 0, 'max': 1},
        },
    }
