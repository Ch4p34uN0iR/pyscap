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

from scap.model.oval_5.sc.EntityItemType import EntityItemType

logger = logging.getLogger(__name__)
class EntityItemSystemMetricIndexType(EntityItemType):
    MODEL_MAP = {
        'elements': [
        ],
        'attributes': {
        },
    }

    def get_value_enumeration(self):
        return [
            'SM_ARRANGE',
            'SM_CLEANBOOT',
            'SM_CMONITORS',
            'SM_CMOUSEBUTTONS',
            'SM_CXBORDER',
            'SM_CXCURSOR',
            'SM_CXDLGFRAME',
            'SM_CXDOUBLECLK',
            'SM_CXDRAG',
            'SM_CXEDGE',
            'SM_CXFIXEDFRAME',
            'SM_CXFOCUSBORDER',
            'SM_CXFRAME',
            'SM_CXFULLSCREEN',
            'SM_CXHSCROLL',
            'SM_CXHTHUMB',
            'SM_CXICON',
            'SM_CXICONSPACING',
            'SM_CXMAXIMIZED',
            'SM_CXMAXTRACK',
            'SM_CXMENUCHECK',
            'SM_CXMENUSIZE',
            'SM_CXMIN',
            'SM_CXMINIMIZED',
            'SM_CXMINSPACING',
            'SM_CXMINTRACK',
            'SM_CXPADDEDBORDER',
            'SM_CXSCREEN',
            'SM_CXSIZE',
            'SM_CXSIZEFRAME',
            'SM_CXSMICON',
            'SM_CXSMSIZE',
            'SM_CXVIRTUALSCREEN',
            'SM_CXVSCROLL',
            'SM_CYBORDER',
            'SM_CYCAPTION',
            'SM_CYCURSOR',
            'SM_CYDLGFRAME',
            'SM_CYDOUBLECLK',
            'SM_CYDRAG',
            'SM_CYEDGE',
            'SM_CYFIXEDFRAME',
            'SM_CYFOCUSBORDER',
            'SM_CYFRAME',
            'SM_CYFULLSCREEN',
            'SM_CYHSCROLL',
            'SM_CYICON',
            'SM_CYICONSPACING',
            'SM_CYKANJIWINDOW',
            'SM_CYMAXIMIZED',
            'SM_CYMAXTRACK',
            'SM_CYMENU',
            'SM_CYMENUCHECK',
            'SM_CYMENUSIZE',
            'SM_CYMIN',
            'SM_CYMINIMIZED',
            'SM_CYMINSPACING',
            'SM_CYMINTRACK',
            'SM_CYSCREEN',
            'SM_CYSIZE',
            'SM_CYSIZEFRAME',
            'SM_CYSMCAPTION',
            'SM_CYSMICON',
            'SM_CYSMSIZE',
            'SM_CYVIRTUALSCREEN',
            'SM_CYVSCROLL',
            'SM_CYVTHUMB',
            'SM_DBCSENABLED',
            'SM_DEBUG',
            'SM_DIGITIZER',
            'SM_IMMENABLED',
            'SM_MAXIMUMTOUCHES',
            'SM_MEDIACENTER',
            'SM_MENUDROPALIGNMENT',
            'SM_MIDEASTENABLED',
            'SM_MOUSEPRESENT',
            'SM_MOUSEHORIZONTALWHEELPRESENT',
            'SM_MOUSEWHEELPRESENT',
            'SM_NETWORK',
            'SM_PENWINDOWS',
            'SM_REMOTECONTROL',
            'SM_REMOTESESSION',
            'SM_SAMEDISPLAYFORMAT',
            'SM_SECURE',
            'SM_SERVERR2',
            'SM_SHOWSOUNDS',
            'SM_SHUTTINGDOWN',
            'SM_SLOWMACHINE',
            'SM_STARTER',
            'SM_SWAPBUTTON',
            'SM_TABLETPC',
            'SM_XVIRTUALSCREEN',
            'SM_YVIRTUALSCREEN',
            '',
        ]

