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
from scap.model.oval_5.sc.independent import *
from scap.model.oval_5.sc.EntityItemStringType import EntityItemStringType

logger = logging.getLogger(__name__)
class EntityItemLdaptypeType(EntityItemStringType):
    MODEL_MAP = {
        'elements': [
        ],
        'attributes': {
        },
    }

    def get_value_enum(self):
        return [
            'LDAPTYPE_ACI_ITEM',
            'LDAPTYPE_ACCESS_POINT',
            'LDAPTYPE_ATTRIBUTE_TYPE_DESCRIP_STRING',
            'LDAPTYPE_AUDIO',
            'LDAPTYPE_BINARY',
            'LDAPTYPE_BIT_STRING',
            'LDAPTYPE_BOOLEAN',
            'LDAPTYPE_CERTIFICATE',
            'LDAPTYPE_CERTIFICATE_LIST',
            'LDAPTYPE_CERTIFICATE_PAIR',
            'LDAPTYPE_COUNTRY_STRING',
            'LDAPTYPE_DN_STRING',
            'LDAPTYPE_DATA_QUALITY_SYNTAX',
            'LDAPTYPE_DELIVERY_METHOD',
            'LDAPTYPE_DIRECTORY_STRING',
            'LDAPTYPE_DIR_CONTENT_RULE_DESCRIPTION',
            'LDAPTYPE_DIT_STRUCTURE_RULE_DESCRIPTION',
            'LDAPTYPE_DL_SUBMIT_PERMISSION',
            'LDAPTYPE_DSA_QUALITY_SYNTAX',
            'LDAPTYPE_DSE_TYPE',
            'LDAPTYPE_ENHANCED_GUIDE',
            'LDAPTYPE_FAX_TEL_NUMBER',
            'LDAPTYPE_FAX',
            'LDAPTYPE_GENERALIZED_TIME',
            'LDAPTYPE_GUIDE',
            'LDAPTYPE_IA5_STRING',
            'LDAPTYPE_INTEGER',
            'LDAPTYPE_JPEG',
            'LDAPTYPE_LDAP_SYNTAX_DESCRIPTION',
            'LDAPTYPE_LDAP_SCHEMA_DEFINITION',
            'LDAPTYPE_LDAP_SCHEMA_DESCRIPTION',
            'LDAPTYPE_MASTER_AND_SHADOW_ACCESS_POINTS',
            'LDAPTYPE_MATCHING_RULE_DESCRIPTION',
            'LDAPTYPE_MATCHING_RULE_USE_DESCRIPTION',
            'LDAPTYPE_MAIL_PREFERENCE',
            'LDAPTYPE_MHS_OR_ADDRESS',
            'LDAPTYPE_MODIFY_RIGHTS',
            'LDAPTYPE_NAME_AND_OPTIONAL_UID',
            'LDAPTYPE_NAME_FORM_DESCRIPTION',
            'LDAPTYPE_NUMERIC_STRING',
            'LDAPTYPE_OBJECT_CLASS_DESCRIP_STRING',
            'LDAPTYPE_OCTET_STRING',
            'LDAPTYPE_OID',
            'LDAPTYPE_MAILBOX',
            'LDAPTYPE_POSTAL_ADDRESS',
            'LDAPTYPE_PROTOCOL_INFORMATION',
            'LDAPTYPE_PRESENTATION_ADDRESS',
            'LDAPTYPE_PRINTABLE_STRING',
            'LDAPTYPE_SUBSTRING_ASSERTION',
            'LDAPTYPE_SUBTREE_SPECIFICATION',
            'LDAPTYPE_SUPPLIER_INFORMATION',
            'LDAPTYPE_SUPPLIER_OR_CONSUMER',
            'LDAPTYPE_SUPPLIER_AND_CONSUMER',
            'LDAPTYPE_SUPPORTED_ALGORITHM',
            'LDAPTYPE_TELEPHONE_NUMBER',
            'LDAPTYPE_TELEX_TERMINAL_ID',
            'LDAPTYPE_TELEX_NUMBER',
            'LDAPTYPE_UTC_TIME',
            'LDAPTYPE_TIMESTAMP',
            'LDAPTYPE_EMAIL',
            '',
        ]
