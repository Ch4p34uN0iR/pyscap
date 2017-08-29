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
import re

from scap.model.decorators import *

from .DurationType import DurationType

logger = logging.getLogger(__name__)

class YearMonthDurationType(DurationType):
    def parse_value(self, value):
        m = re.fullmatch(r'-?P(\d+Y)?(\d+M)?', value)
        if not m or not re.fullmatch(r'.*[YM].*', value):
            raise ValueError('Unable to parse xs:YearMonthDuration value')

        return super(YearMonthDurationType, self).parse_value(value)

    def produce_value(self, value):
        months, seconds = value
        if seconds != 0:
            raise ValueError('xs:YearMonthDuration requires 0 for seconds value')

        return super(YearMonthDurationType, self).produce_value(value)
