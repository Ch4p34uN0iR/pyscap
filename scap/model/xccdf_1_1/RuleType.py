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

from scap.model.xccdf_1_1.SelectableItemType import SelectableItemType
from scap.model.xccdf_1_1.RoleEnumeration import ROLE_ENUMERATION
from scap.model.xccdf_1_1.SeverityEnumeration import SEVERITY_ENUMERATION
from scap.Model import Model
import logging

logger = logging.getLogger(__name__)
class RuleType(SelectableItemType):
    MODEL_MAP = {
        'attributes': {
            'id': {'required': True, 'type': 'RuleIDPattern'},
            'role': {'enum': ROLE_ENUMERATION, 'default': 'full'},
            'severity': {'enum': SEVERITY_ENUMERATION, 'default': 'unknown'},
            'multiple': {'type': 'Boolean', 'default': False},
        },
        'elements': {
            '{http://checklists.nist.gov/xccdf/1.1}ident': {'append': 'idents', 'min': 0, 'max': None, 'class': 'IdentType'},
            '{http://checklists.nist.gov/xccdf/1.1}impact-metric': {'min': 0, 'max': 1, 'type': 'String'},
            '{http://checklists.nist.gov/xccdf/1.1}profile-note': {'append': 'profile_notes', 'ignore': True, 'min': 0, 'max': None, 'class': 'ProfileNoteType'},
            '{http://checklists.nist.gov/xccdf/1.1}fix': {'class': 'FixType', 'min': 0, 'max': None, 'append': 'fixes'},
            '{http://checklists.nist.gov/xccdf/1.1}fixtext': {'class': 'FixtextType', 'min': 0, 'max': None, 'append': 'fixtexts'},
            '{http://checklists.nist.gov/xccdf/1.1}check': {'class': 'CheckType', 'min': 0, 'max': None, 'map': 'checks', 'key': 'selector'},
            '{http://checklists.nist.gov/xccdf/1.1}complex-check': {'class': 'ComplexCheckType', 'min': 0, 'max': 1},
            '{http://checklists.nist.gov/xccdf/1.1}signature': {'ignore': True, 'class': 'SignatureType', 'min': 0, 'max': 1},
        },
    }

    def __init__(self):
        super(RuleType, self).__init__()

        self.check_selector = None

    def process(self, benchmark):
        super(RuleType, self).process(benchmark)

        if not self._continue_processing():
            return

        ### Rule.Content

        # If the Item is a Rule, then process the properties of the Rule.
        # TODO

        ### Default Model
        # urn:xccdf:scoring:default

            ### Score.Rule

            ### Score.Group.Init

            ### Score.Group.Recurse

            ### Score.Group.Normalize

            ### Score.Weight

        ### Flat Model
        # urn:xccdf:scoring:flat

            ### Score.Init

            ### Score.Rules

        ### Flat Unweighted Model
        # urn:xccdf:scoring:flat-unweighted

        ### Absolute Model
        # urn:xccdf:scoring:absolute
        import inspect
        raise NotImplementedError(inspect.stack()[0][3] + '() has not been implemented in subclass: ' + self.__class__.__name__)
