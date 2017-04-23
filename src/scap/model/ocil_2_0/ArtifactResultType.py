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

from scap.Model import Model
import logging

logger = logging.getLogger(__name__)
class ArtifactResultType(Model):
    MODEL_MAP = {
        'elements': [
            # children of artifact_value tag
            # TODO: at least one of *_artifact_value
            {'xml_namespace': 'http://scap.nist.gov/schema/ocil/2.0', 'tag_name': 'text_artifact_value', 'class': 'TextArtifactValueElement', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://scap.nist.gov/schema/ocil/2.0', 'tag_name': 'binary_artifact_value', 'class': 'BinaryArtifactValueElement', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://scap.nist.gov/schema/ocil/2.0', 'tag_name': 'reference_artifact_value', 'class': 'ReferenceArtifactValueElement', 'min': 0, 'max': 1},
            {'xml_namespace': 'http://scap.nist.gov/schema/ocil/2.0', 'tag_name': 'provider', 'type': 'ProviderValuePattern', 'min': 1, 'max': 1},
            {'xml_namespace': 'http://scap.nist.gov/schema/ocil/2.0', 'tag_name': 'submitter', 'class': 'UserType', 'min': 1, 'max': 1},
        ],
        'attributes': {
            'artifact_ref': {'type': 'ArtifactIDPattern', 'required': True},
            'timestamp': {'type': 'DateTime', 'required': True},
        }
    }
