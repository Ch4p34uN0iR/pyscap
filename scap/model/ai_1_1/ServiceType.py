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

from scap.model.ai_1_1.ITAssetType import ITAssetType
import logging
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)
class ServiceType(ITAssetType):
    MODEL_MAP = {
        'tag_name': 'service',
        'elements': [
            {'tag_name': 'host', 'class': 'HostType', 'min': 0},
            {'tag_name': 'port', 'list': 'ports', 'class': 'ServicePortType', 'min': 0, 'max': None},
            {'tag_name': 'port-range', 'list': 'port_ranges', 'class': 'PortRangeType', 'min': 0, 'max': None},
            {'tag_name': 'protocol', 'class': 'ProtocolType', 'min': 0},
        ],
    }
