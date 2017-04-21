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
from scap.model.xccdf_1_1.ResultEnumeration import RESULT_ENUMERATION
from scap.model.xccdf_1_1.RoleEnumeration import ROLE_ENUMERATION
from scap.model.xccdf_1_1.SeverityEnumeration import SEVERITY_ENUMERATION

logger = logging.getLogger(__name__)
class RuleResultType(Model):
    MODEL_MAP = {
        'elements': {
            '{http://checklists.nist.gov/xccdf/1.1}result': {'enum': RESULT_ENUMERATION, 'min': 1, 'max': 1},
            '{http://checklists.nist.gov/xccdf/1.1}override': {'class': 'OverrideType', 'append': 'overrides', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}ident': {'class': 'IdentType', 'append': 'idents', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}message': {'class': 'MessageType', 'append': 'messages', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}instance': {'class': 'InstanceResultType', 'append': 'instances', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}fix': {'class': 'FixType', 'append': 'fixes', 'min': 0, 'max': None},
            '{http://checklists.nist.gov/xccdf/1.1}check': {'class': 'CheckType', 'append': 'checks', 'min': 0, 'max': None},
        },
        'element_order': [],
        'attributes': {
            'idref': {'type': 'NCName', 'required': True},
            'role': {'enum': ROLE_ENUMERATION},
            'severity': {'enum': SEVERITY_ENUMERATION},
            'time': {'type': 'DateTime'},
            'version': {'type': 'String'},
            'weight': {'type': 'WeightType'},
        },
    }
