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

RATING_ENUMERATION = [
    'unknown',
    # rating unknown or impossible to estimate (default for forward
    # compatibility for XCCDF 1.0)
    'low',
    # little or no potential for disruption, very modest complexity
    'medium',
    # some chance of minor disruption,  substantial complexity
    'high',
    # likely to cause serious disruption, very complex
]
