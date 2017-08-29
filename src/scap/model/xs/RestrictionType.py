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

from scap.model.decorators import *
from scap.model.types import *

from .AnnotatedType import AnnotatedType
from .ChoiceElement import ChoiceElement
from .FacetType import FacetType
from .GroupType import GroupType
from .GroupType import GroupType
from .PatternElement import PatternElement
from .TotalDigitsElement import TotalDigitsElement
from .WhitespaceElement import WhitespaceElement
from .WildcardType import WildcardType

logger = logging.getLogger(__name__)

@attribute(local_name='base', type=QNameType)
@element(local_name='group', list='tags', cls=GroupType, min=0)
@element(local_name='all', list='tags',
    cls=defer_class_load('scap.model.xs.AllType', 'AllType'),
    min=0)
@element(local_name='choice', list='tags', cls=ChoiceElement, min=0)
@element(local_name='sequence', list='tags', cls=GroupType, min=0)
@element(local_name='simpleType', list='tags',
    cls=defer_class_load('scap.model.xs.SimpleTypeType', 'SimpleTypeType'),
    min=0)
@element(local_name='minExclusive', list='tags', cls=FacetType, min=0, max=None)
@element(local_name='minInclusive', list='tags', cls=FacetType, min=0, max=None)
@element(local_name='maxExclusive', list='tags', cls=FacetType, min=0, max=None)
@element(local_name='maxInclusive', list='tags', cls=FacetType, min=0, max=None)
@element(local_name='totalDigits', list='tags', cls=TotalDigitsElement, min=0, max=None)
@element(local_name='fractionDigits', list='tags', cls=FacetType, min=0, max=None)
@element(local_name='length', list='tags', cls=FacetType, min=0, max=None)
@element(local_name='minLength', list='tags', cls=FacetType, min=0, max=None)
@element(local_name='maxLength', list='tags', cls=FacetType, min=0, max=None)
@element(local_name='enumeration', list='tags', cls=FacetType, min=0, max=None)
@element(local_name='whiteSpace', list='tags', cls=WhitespaceElement, min=0, max=None)
@element(local_name='pattern', list='tags', cls=PatternElement, min=0, max=None)
@element(local_name='attribute', list='tags',
    cls=defer_class_load('scap.model.xs.AttributeType', 'AttributeType'),
    min=0, max=None)
@element(local_name='attributeGroup', list='tags',
    cls=defer_class_load('scap.model.xs.AttributeGroupType', 'AttributeGroupType'),
    min=0, max=None)
@element(local_name='anyAttribute', list='tags', cls=WildcardType, min=0)
class RestrictionType(AnnotatedType):
    def get_defs(self, schema, top_level):
        logger.debug('Base: ' + self.base)
        # TODO unable to map xmlns because ET doesn't retain it
        base_ns, base_name = [self.base.partition(':')[i] for i in [0,2]]
        top_level.set_super_module(base_ns)
        top_level.set_super_class(base_name)

        return super(RestrictionType, self).get_defs(schema, top_level)
