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
from scap.model.decorators import *
from scap.model.oval_5.sc.ItemType import ItemType

logger = logging.getLogger(__name__)

class LdapItemElement(ItemType):
    MODEL_MAP = {
        'elements': [
@element(local_name='suffix', cls=scap.model.oval_5.sc.EntityItemType, min=0, max=1)
@element(local_name='relative_dn', cls=scap.model.oval_5.sc.EntityItemType, min=0, max=1, 'nillable': True)
@element(local_name='attribute', cls=scap.model.oval_5.sc.EntityItemType, min=0, max=1, 'nillable': True)
@element(local_name='object_class', cls=scap.model.oval_5.sc.EntityItemType, min=0, max=1)
@element(local_name='ldaptype', cls=EntityItemLdaptypeType, min=0, max=1)
@element(local_name='value', cls=scap.model.oval_5.sc.EntityItemType, min=0, max=None)
        ],
        'attributes': {
        }
    }
