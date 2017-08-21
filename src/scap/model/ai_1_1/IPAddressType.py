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
from scap.Model import Model

from .IPAddressIPv4Type import IPAddressIPv4Type
from .IPAddressIPv6Type import IPAddressIPv6Type

logger = logging.getLogger(__name__)

@element(local_name='ip-v4', cls=IPAddressIPv4Type, min=0)
@element(local_name='ip-v6', cls=IPAddressIPv6Type, min=0)
class IPAddressType(Model):
    # collapsed ip-address element into ip-address-type
    pass
