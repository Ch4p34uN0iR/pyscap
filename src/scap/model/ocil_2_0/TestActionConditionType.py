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

logger = logging.getLogger(__name__)

class TestActionConditionType(Model):
    MODEL_MAP = {
        'elements': [
            # TODO: at least one result or test_action_ref
            {'tag_name': 'result', 'class': 'ResultType', 'min': 0, 'max': 1},
            {'tag_name': 'test_action_ref', 'class': 'TestActionRefType', 'min': 0, 'max': 1},
            {'tag_name': 'artifact_refs', 'class': 'ArtifactRefsType', 'min': 0, 'max': 1},
        ],
    }
