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

from ..EntityItemType import EntityItemType import EntityItemType

logger = logging.getLogger(__name__)

class EntityItemServiceTypeType(EntityItemType):
    MODEL_MAP = {
        'elements': [
        ],
        'attributes': {
        },
    }

    def get_value_enum(self):
        return [
            'SERVICE_FILE_SYSTEM_DRIVER',
            'SERVICE_KERNEL_DRIVER',
            'SERVICE_WIN32_OWN_PROCESS',
            'SERVICE_WIN32_SHARE_PROCESS',
            'SERVICE_INTERACTIVE_PROCESS',
            '',
        ]
