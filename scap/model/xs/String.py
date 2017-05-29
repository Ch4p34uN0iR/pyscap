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

from scap.model.xs.AnySimpleType import AnySimpleType

logger = logging.getLogger(__name__)
class String(AnySimpleType):
    def get_value_pattern(self):
        return None

    def parse_value(self, value):
        if not isinstance(value, str):
            raise TypeError('xs:string requires a str for initialization, got ' + value.__class__.__name__)

        p = self.get_value_pattern()
        if not re.fullmatch(p, value):
            raise ValueError(self.__class__.__name__ + ' requires a str matching ' + p)

        return value
