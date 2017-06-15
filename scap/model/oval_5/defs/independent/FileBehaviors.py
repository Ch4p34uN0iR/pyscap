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

logger = logging.getLogger(__name__)
class FileBehaviors(Model):
    MODEL_MAP = {
        'attributes': {
            'max_depth': {'type': 'Integer', 'default': -1},
            'recurse': {'enum': ['directories', 'symlinks', 'symlinks and directories'], 'default': 'symlinks and directories'},
            'recurse_direction': {'enum': ['none', 'up', 'down'], 'default': 'none'},
            'recurse_file_system': {'enum': ['all', 'local', 'defined'], 'default': 'all'},
            'windows_view': {'enum': ['32_bit', '64_bit'], 'default': '64_bit'},
        }
    }
