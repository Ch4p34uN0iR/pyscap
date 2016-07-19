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
from scap.Engine import Engine

logger = logging.getLogger(__name__)
class Catalog(Model):
    def from_xml(self, parent, el):
        super(self.__class__, self).from_xml(parent, el)

        self.entries = {}
        for entry in el.findall('./xml_cat:uri', Engine.namespaces):
            self.entries[entry.attrib['name']] = entry.attrib['uri']

    def to_dict(self):
        logger.debug('Catalog entries: ' + str(self.entries))
        return self.entries