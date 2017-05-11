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

from scap.model.xccdf_1_2.ItemType import ItemType
from scap.model.xccdf_1_2.ValueTypeEnumeration import VALUE_TYPE_ENUMERATION
from scap.model.xccdf_1_2.ValueOperatorEnumeration import VALUE_OPERATOR_ENUMERATION
from scap.model.xccdf_1_2.InterfaceHintEnumeration import INTERFACE_HINT_ENUMERATION
import logging

logger = logging.getLogger(__name__)
class ValueType(ItemType):
    MODEL_MAP = {
        'attributes': {
            'id': {'type': 'ValueIDPattern', 'required': True},
            'type': {'enum': VALUE_TYPE_ENUMERATION, 'default': 'string'},
            'operator': {'enum': VALUE_OPERATOR_ENUMERATION, 'default': 'equals'},
            'interactive': {'type': 'Boolean'},
            'interfaceHint': {'enum': INTERFACE_HINT_ENUMERATION},
        },
        'elements': [
            # TODO: at least one value
            # TODO: since order matters in xml (and for values) we might need a list vs. dict here
            {'tag_name': 'value', 'class': 'SelStringType', 'dict': 'values', 'key': 'selector', 'min': 0, 'max': None},
            {'tag_name': 'complex-value', 'class': 'SelComplexValueType', 'dict': 'complex_values', 'key': 'selector', 'min': 0, 'max': None},
            # choice of below
            {'tag_name': 'default', 'class': 'SelStringType', 'min': 0, 'max': None, 'dict': 'defaults', 'key': 'selector'},
            {'tag_name': 'complex-default', 'class': 'SelComplexValueType', 'min': 0, 'max': None, 'dict': 'complex_defaults', 'key': 'selector'},
            {'tag_name': 'match', 'class': 'SelStringType', 'dict': 'matches', 'key': 'selector', 'min': 0, 'max': None},
            {'tag_name': 'lower-bound', 'class': 'SelNumType', 'dict': 'lower_bounds', 'key': 'selector', 'min': 0, 'max': None},
            {'tag_name': 'upper-bound', 'class': 'SelNumType', 'dict': 'upper_bounds', 'key': 'selector', 'min': 0, 'max': None},
            {'tag_name': 'choices', 'class': 'SelChoicesType', 'dict': 'choices', 'key': 'selector', 'min': 0, 'max': None},
            {'tag_name': 'source', 'class': 'URIRefType', 'list': 'sources', 'min': 0, 'max': None},
            {'tag_name': 'signature', 'class': 'SignatureType', 'min': 0, 'max': None},
        ],
    }
