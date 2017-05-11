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
from scap.model.xccdf_1_1.CheckOperatorEnumeration import CHECK_OPERATOR_ENUMERATION, AND, OR, negate

logger = logging.getLogger(__name__)
class ComplexCheckType(Model):
    MODEL_MAP = {
        'elements': [
            # TODO: ensure checks has at least 1
            {'tag_name': 'check', 'class': 'CheckType', 'min': 0, 'max': None, 'list': 'checks'},
            {'tag_name': 'complex-check', 'class': 'ComplexCheckType', 'min': 0, 'max': None, 'list': 'checks'},
        ],
        'attributes': {
            'operator': {'enum': CHECK_OPERATOR_ENUMERATION, 'required': True},
            'negate': {'type': 'Boolean', 'default': False},
        },
    }


    def check(self, benchmark, host):
        if len(self.checks) < 1:
            raise ValueError('No sub-checks with complex-check')

        check_results = []
        for check in self.checks:
            check_results += check.check(benchmark, host)

        # apply the operator
        if self.operator == 'AND':
            result = AND([x['result'] for x in check_results])
        elif self.operator == 'OR':
            result = OR([x['result'] for x in check_results])
        else:
            raise ValueError('Unknown check operator: ' + self.operator)

        if self.negate:
            result = negate(result)

        return {
            'result': result,
            'message': 'Complex check results',
            'imports': {}
        }
