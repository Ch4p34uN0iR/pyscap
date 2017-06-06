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
TAG_MAP = {
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}environmentvariable_test': 'EnvironmentVariableTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}environmentvariable58_test': 'EnvironmentVariable58TestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}family_test': 'FamilyTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}filehash58_test': 'FileHash58TestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}filehash_test': 'FileHashTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}ldap57_test': 'LDAP57TestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}ldap_test': 'LDAPTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}sql57_test': 'SQL57TestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}sql_test': 'SQLTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}textfilecontent54_test': 'TextFileContent54TestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}textfilecontent_test': 'TextFileContentTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}unknown_test': 'UnknownTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}variable_test': 'VariableTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}xmlfilecontent_test': 'XMLFileContentTestElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}environmentvariable_object': 'EnvironmentVariableObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}environmentvariable58_object': 'EnvironmentVariable58ObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}family_object': 'FamilyObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}filehash58_object': 'FileHash58ObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}filehash_object': 'FileHashObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}ldap57_object': 'LDAP57ObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}ldap_object': 'LDAPObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}sql57_object': 'SQL57ObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}sql_object': 'SQLObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}textfilecontent54_object': 'TextFileContent54ObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}textfilecontent_object': 'TextFileContentObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}variable_object': 'VariableObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}xmlfilecontent_object': 'XMLFileContentObjectElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}environmentvariable_state': 'EnvironmentVariableStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}environmentvariable58_state': 'EnvironmentVariable58StateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}family_state': 'FamilyStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}filehash58_state': 'FileHash58StateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}filehash_state': 'FileHashStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}ldap57_state': 'LDAP57StateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}ldap_state': 'LDAPStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}sql57_state': 'SQL57StateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}sql_state': 'SQLStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}textfilecontent54_state': 'TextFileContent54StateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}textfilecontent_state': 'TextFileContentStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}variable_state': 'VariableStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#independent}xmlfilecontent_state': 'XMLFileContentStateElement',
}

ENGINE_ENUMERATION = [
    'access',
    'db2',
    'cache',
    'firebird',
    'firstsql',
    'foxpro',
    'informix',
    'ingres',
    'interbase',
    'lightbase',
    'maxdb',
    'monetdb',
    'mimer',
    'mysql',
    'oracle',
    'paradox',
    'pervasive',
    'postgre',
    'sqlbase',
    'sqlite',
    'sqlserver',
    'sybase',
    '',
]

RECURSE_DIRECTION = [
    'none',
    'up',
    'down',
]

RECURSE_FILE_SYSTEM = [
    'all',
    'local',
    'defined',
]

WINDOWS_VIEW = [
    '32_bit',
    '64_bit',
]

from scap.model.oval_5 import FAMILY_ENUMERATION

HASH_ENUMERATION = [
    'MD5',
    'SHA-1',
    'SHA-224',
    'SHA-256',
    'SHA-384',
    'SHA-512',
    '',
]

LDAP_TYPE_ENUMERATION = [
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

WINDOWS_VIEW_ENUMERATION = [
    '32_bit',
    '64_bit',
    '',
]