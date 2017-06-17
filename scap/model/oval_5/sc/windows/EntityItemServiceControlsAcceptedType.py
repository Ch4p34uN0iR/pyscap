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

from scap.model.oval_5.sc.EntityItemStringType import EntityItemStringType

logger = logging.getLogger(__name__)
class EntityItemServiceControlsAcceptedType(EntityItemStringType):
    MODEL_MAP = {
        'elements': [
        ],
        'attributes': {
        },
    }

    def get_value_enumeration(self):
        return [
            'SERVICE_ACCEPT_NETBINDCHANGE',
            'SERVICE_ACCEPT_PARAMCHANGE',
            'SERVICE_ACCEPT_PAUSE_CONTINUE',
            'SERVICE_ACCEPT_PRESHUTDOWN',
            'SERVICE_ACCEPT_SHUTDOWN',
            'SERVICE_ACCEPT_STOP',
            'SERVICE_ACCEPT_HARDWAREPROFILECHANGE',
            'SERVICE_ACCEPT_POWEREVENT',
            'SERVICE_ACCEPT_SESSIONCHANGE',
            'SERVICE_ACCEPT_TIMECHANGE',
            'SERVICE_ACCEPT_TRIGGEREVENT',
            '',
        ]
