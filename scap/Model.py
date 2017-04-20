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
import importlib
import sys
import xml.etree.ElementTree as ET

from scap.model import NAMESPACES

XML_SPACE_ENUMERATION = [
    'default',
    # The value "default" signals that applications' default white-space
    # processing modes are acceptable for this element
    'preserve',
    # the value "preserve" indicates the intent that applications preserve all
    # the white space
]

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
class Model(object):
    MODEL_MAP = {
        'attributes': {
            '{http://www.w3.org/XML/1998/namespace}lang': {'type': 'String'},
            '{http://www.w3.org/XML/1998/namespace}space': {'enum': XML_SPACE_ENUMERATION, 'default': 'default'},
            '{http://www.w3.org/XML/1998/namespace}base': {'type': 'AnyURI'},
            '{http://www.w3.org/XML/1998/namespace}id': {'type': 'ID'},
            '{http://www.w3.org/2001/XMLSchema-instance}schemaLocation': {'type': 'AnyURI'},
        },
    }

    maps = {}
    content_cache = {}
    index = {}

    @staticmethod
    def parse_tag(tag):
        # parse tag
        if tag.startswith('{'):
            xml_namespace, tag_name = tag[1:].split('}')
        else:
            return None, tag

        if xml_namespace not in NAMESPACES:
            logger.critical('Unsupported namespace: ' + xml_namespace + ', tag name: ' + tag_name)
            sys.exit()

        return xml_namespace, tag_name

    @staticmethod
    def load(parent, child_el, uri=None):
        xml_namespace, tag_name = Model.parse_tag(child_el.tag)

        if xml_namespace not in NAMESPACES:
            raise NotImplementedError('Namespace ' + xml_namespace + ' is not supported')
        model_namespace = NAMESPACES[xml_namespace]

        # try to load the tag's module
        if parent is None:
            # look up from __init__ file
            pkg_mod = importlib.import_module('scap.model.' + model_namespace)
            try:
                module_name = pkg_mod.TAG_MAP[child_el.tag]['class']
            except AttributeError:
                logger.critical(pkg_mod.__name__ + ' does not define TAG_MAP; cannot load ' + child_el.tag)
                sys.exit()
            except KeyError:
                logger.critical(pkg_mod.__name__ + ' does not define mapping for ' + child_el.tag + ' tag')
                sys.exit()
        else:
            mmap = Model._get_model_map(parent.__class__)
            ns_any = '{' + xml_namespace + '}*'

            logger.debug('Checking ' + parent.__class__.__name__ + ' for tag ' + child_el.tag)
            module_name = None
            for name in [child_el.tag, tag_name, ns_any, '*']:
                if name not in mmap['elements']:
                    continue

                logger.debug(child_el.tag + ' matched ' + name + ' mapping in ' + parent.__class__.__name__)
                if name.endswith('*'):
                    # look up from __init__ file
                    pkg_mod = importlib.import_module('scap.model.' + model_namespace)
                    try:
                        module_name = pkg_mod.TAG_MAP[child_el.tag]['class']
                    except AttributeError:
                        logger.critical(pkg_mod.__name__ + ' does not define TAG_MAP; cannot load ' + child_el.tag)
                        sys.exit()
                    except KeyError:
                        logger.critical(pkg_mod.__name__ + ' does not define mapping for ' + child_el.tag + ' tag')
                        sys.exit()
                    break
                elif 'class' in mmap['elements'][name]:
                    module_name = mmap['elements'][child_el.tag]['class']
                    break

            if module_name is None:
                logger.debug('Did not match any of ' + str([child_el.tag, tag_name, ns_any, '*']))
                logger.critical(parent.__class__.__name__ + ' does not define mapping for ' + child_el.tag + ' tag')
                sys.exit()

        if '.' in module_name:
            model_module = 'scap.model.' + module_name
            module_name = module_name.partition('.')[2]
        else:
            model_module = 'scap.model.' + model_namespace + '.' + module_name

        if model_module not in sys.modules:
            logger.debug('Loading module ' + model_module)

            mod = importlib.import_module(model_module)
        else:
            mod = sys.modules[model_module]

        # instantiate an instance of the class & load it
        class_ = getattr(mod, module_name)
        inst = class_()
        inst.from_xml(parent, child_el)

        if parent is None:
            Model.content_cache[uri] = inst

        return inst

    @staticmethod
    def _get_model_map(model_class):
        fq_model_class_name = model_class.__module__ + '.' + model_class.__name__
        if fq_model_class_name not in Model.maps:
            at_map = {}
            el_map = {}
            xml_namespace = None
            tag_name = None
            for class_ in model_class.__mro__:
                if class_ == object:
                    break

                if class_.__module__.startswith('collections.'):
                    # skip collection classes
                    continue

                fq_class_name = class_.__module__ + '.' + class_.__name__

                try:
                    class_.MODEL_MAP
                except AttributeError:
                    logger.critical('Class ' + fq_class_name + ' does not define MODEL_MAP')
                    sys.exit()

                # overwrite the super class' ns & tag with what we've already loaded
                try:
                    if xml_namespace is None:
                        xml_namespace = class_.MODEL_MAP['xml_namespace']
                except KeyError:
                    #logger.debug('Class ' + fq_class_name + ' does not have MODEL_MAP[xml_namespace] defined')
                    pass
                try:
                    if tag_name is None:
                        tag_name = class_.MODEL_MAP['tag_name']
                except KeyError:
                    #logger.debug('Class ' + fq_class_name + ' does not have MODEL_MAP[tag_name] defined')
                    pass

                # update the super class' attribute map with subclass
                try:
                    super_atmap = class_.MODEL_MAP['attributes'].copy()
                    super_atmap.update(at_map)
                    at_map = super_atmap
                except KeyError:
                    #logger.debug('Class ' + fq_class_name + ' does not have MODEL_MAP[attributes] defined')
                    pass

                # update the super class' element map with subclass
                try:
                    super_elmap = class_.MODEL_MAP['elements'].copy()
                    super_elmap.update(el_map)
                    el_map = super_elmap
                except KeyError:
                    #logger.debug('Class ' + fq_class_name + ' does not have MODEL_MAP[elements] defined')
                    pass

            if xml_namespace is None:
                # try to auto detect from module name
                NAMESPACES_reverse = {v: k for k, v in NAMESPACES.items()}
                module_parts = model_class.__module__.split('.')
                if module_parts[0] == 'scap' and module_parts[1] == 'model' and module_parts[2] in NAMESPACES_reverse:
                    logger.debug('Found xml namespace ' + NAMESPACES_reverse[module_parts[2]] + ' for model namespace ' + module_parts[2])
                    xml_namespace = NAMESPACES_reverse[module_parts[2]]

            Model.maps[fq_model_class_name] = {
                'xml_namespace': xml_namespace,
                'tag_name': tag_name,
                'attributes': at_map,
                'elements': el_map,
            }
        return Model.maps[fq_model_class_name]

    @staticmethod
    def find_content(uri):
        if uri in Model.content_cache:
            return Model.content_cache[uri]
        else:
            return None

    def __init__(self, tag_name=None):
        self.parent = None
        self.sub_references = {}
        self.text = None
        self.tail = None
        self.model_map = Model._get_model_map(self.__class__)
        if tag_name is not None:
            self.tag_name = tag_name

        # must have namespace for concrete classes
        if 'xml_namespace' not in self.model_map or self.model_map['xml_namespace'] is None:
            raise ValueError('No xml_namespace defined for ' + self.__class__.__name__ + ' & could not detect')

        if self.model_map['xml_namespace'] not in NAMESPACES:
            raise ValueError('Unknown namespace: ' + self.model_map['xml_namespace'])

        # initialize attribute values
        for name in self.model_map['attributes']:
            attr_map = self.model_map['attributes'][name]
            if 'in' in attr_map:
                attr_name = attr_map['in']
            else:
                xml_namespace, attr_name = Model.parse_tag(name)
                attr_name = attr_name.replace('-', '_')

            if 'default' in attr_map:
                value = attr_map['default']
                setattr(self, attr_name, value)
                logger.debug('Default of attribute ' + attr_name + ' = ' + str(value))
            else:
                setattr(self, attr_name, None)

        # initialize elements
        for tag in self.model_map['elements']:
            xml_namespace, tag_name = Model.parse_tag(tag)
            tag_map = self.model_map['elements'][tag]

            if tag.endswith('*'):
                if 'in' in tag_map:
                    name = tag_map['in']
                else:
                    name = '_tags'

                if name not in list(self.__dict__.keys()):
                    logger.debug('Initializing ' + name + ' to []')
                    setattr(self, name, [])

            elif 'append' in tag_map:
                # initialze the array if it doesn't exist
                if tag_map['append'] not in list(self.__dict__.keys()):
                    logger.debug('Initializing ' + tag_map['append'] + ' to []')
                    setattr(self, tag_map['append'], [])

            elif 'map' in tag_map:
                # initialze the dict if it doesn't exist
                if tag_map['map'] not in list(self.__dict__.keys()):
                    logger.debug('Initializing ' + tag_map['map'] + ' to {}')
                    setattr(self, tag_map['map'], {})

            else:
                if 'in' in tag_map:
                    name = tag_map['in']
                else:
                    name = tag_name.replace('-', '_')

                if name not in list(self.__dict__.keys()):
                    logger.debug('Initializing ' + name + ' to None')
                    setattr(self, name, None)

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)

        if name == 'id':
            if self.__class__.__name__ not in Model.index:
                Model.index[self.__class__.__name__] = {}
            Model.index[self.__class__.__name__][value] = self

    def accept(self, visitor):
        visitor.visit(self)

    def get_tag_name(self):
        if hasattr(self, 'tag_name'):
            return self.tag_name
        if 'tag_name' not in self.model_map or self.model_map['tag_name'] is None:
            raise NotImplementedError('Subclass ' + self.__class__.__name__ + ' does not define tag_name')
        return self.model_map['tag_name']

    def get_xml_namespace(self):
        if 'xml_namespace' not in self.model_map or self.model_map['xml_namespace'] is None:
            raise NotImplementedError('Subclass ' + self.__class__.__name__ + ' does not define namespace')
        return self.model_map['xml_namespace']

    def get_model_namespace(self):
        xml_namespace = self.get_xml_namespace()
        if xml_namespace not in NAMESPACES:
            raise NotImplementedError('Namespace ' + xml_namespace + ' is not supported')
        return NAMESPACES[xml_namespace]

    def get_tag(self):
        return '{' + self.get_xml_namespace() + '}' + self.get_tag_name()

    def get_text(self):
        return self.text

    def get_tail(self):
        return self.tail

    def from_xml(self, parent, el):
        self.parent = parent

        logger.debug('Parsing ' + el.tag + ' element into ' + self.__class__.__module__ + '.' + self.__class__.__name__ + ' class')

        for attrib in self.model_map['attributes']:
            if 'required' in self.model_map['attributes'][attrib] \
            and self.model_map['attributes'][attrib]['required'] \
            and attrib not in el.keys() \
            and 'default' not in self.model_map['attributes'][attrib]:
                logger.critical(el.tag + ' must define ' + attrib + ' attribute')
                sys.exit()

        for name, value in list(el.items()):
            if not self.parse_attribute(name, value):
                logger.critical('Unknown attrib in ' + el.tag + ': ' + name + ' = ' + value)
                sys.exit()

        sub_el_counts = {}
        for sub_el in el:
            if not self.parse_element(sub_el):
                print(str(self.model_map['elements']))
                logger.critical('Unknown element in ' + el.tag + ': ' + sub_el.tag)
                sys.exit()

            if sub_el.tag not in sub_el_counts:
                sub_el_counts[sub_el.tag] = 1
            else:
                sub_el_counts[sub_el.tag] += 1

        for tag in self.model_map['elements']:
            tag_map = self.model_map['elements'][tag]

            min_ = 1
            if 'map' in tag_map or 'append' in tag_map:
                # maps and appends default to no max
                max_ = None
            else:
                max_ = 1

            if 'min' in tag_map:
                min_ = tag_map['min']
            if 'max' in tag_map:
                max_ = tag_map['max']

            if min_ == 0:
                pass
            elif tag not in sub_el_counts or sub_el_counts[tag] < min_:
                logger.critical(self.__class__.__name__ + ' must have at least ' + str(min_) + ' ' + tag + ' elements')
                sys.exit()

            if max_ is None:
                pass
            elif tag in sub_el_counts and sub_el_counts[tag] > max_:
                logger.critical(self.__class__.__name__ + ' must have at most ' + str(max_) + ' ' + tag + ' elements')
                sys.exit()

        self.text = el.text

    def _parse_value_as_type(self, value, type_):
        if '.' in type_:
            try:
                mod = importlib.import_module('scap.model.' + type_)
                type_ = type_.partition('.')[2]
            except ImportError:
                raise NotImplementedError('Type value scap.model.' + type_ + ' was not found')
        else:
            try:
                mod = importlib.import_module('scap.model.xs_2001.' + type_)
            except ImportError:
                model_namespace = self.get_model_namespace()
                try:
                    mod = importlib.import_module('scap.model.' + model_namespace + '.' + type_)
                except ImportError:
                    raise NotImplementedError('Type value ' + type_ + ' not defined in scap.model.xs_2001 or local namespace (scap.model.' + model_namespace + ')')
        class_ = getattr(mod, type_)
        return class_().parse_value(value)

    def parse_attribute(self, name, value):
        xml_namespace, attr_name = Model.parse_tag(name)

        if xml_namespace is None:
            ns_any = '{' + self.model_map['xml_namespace'] + '}*'
        else:
            ns_any = '{' + xml_namespace + '}*'

        for name in [name, attr_name, ns_any, '*']:
            if name not in self.model_map['attributes']:
                continue

            attr_map = self.model_map['attributes'][name]

            if 'notImplemented' in attr_map and attr_map['notImplemented']:
                raise NotImplementedError(name + ' attribute support is not implemented')

            if 'enum' in attr_map and value not in attr_map['enum']:
                raise ValueError(name + ' attribute must be one of ' + str(attr_map['enum']) + ': ' + str(value))

            # convert value
            if 'type' in attr_map:
                logger.debug('Parsing ' + str(value) + ' as ' + attr_map['type'] + ' type')
                value = self._parse_value_as_type(value, attr_map['type'])

            if 'in' in attr_map:
                setattr(self, attr_map['in'], value)
                logger.debug('Set attribute ' + attr_map['in'] + ' = ' + str(value))
            else:
                name = attr_name.replace('-', '_')
                setattr(self, name, value)
                logger.debug('Set attribute ' + name + ' = ' + str(value))
            return True
        return False

    def parse_element(self, el):
        xml_namespace, tag_name = Model.parse_tag(el.tag)

        if xml_namespace is None:
            ns_any = '{' + self.model_map['xml_namespace'] + '}*'
        else:
            ns_any = '{' + xml_namespace + '}*'

        for tag in [el.tag, tag_name, ns_any, '*']:
            # check both namespace + tag_name and just tag_name
            if tag not in self.model_map['elements']:
                continue

            logger.debug('Tag ' + el.tag + ' matched ' + tag)
            tag_map = self.model_map['elements'][tag]

            if 'notImplemented' in tag_map and tag_map['notImplemented']:
                raise NotImplementedError(tag + ' element support is not implemented')

            if tag.endswith('*'):
                if 'in' in tag_map:
                    name = tag_map['in']
                else:
                    name = '_tags'

                lst = getattr(self, name)

                if '{http://www.w3.org/2001/XMLSchema-instance}nil' in el.keys() and el.get('{http://www.w3.org/2001/XMLSchema-instance}nil') == 'true':
                    # check if we can accept nil
                    if 'nillable' in tag_map and tag_map['nillable']:
                        value = None
                    else:
                        raise ValueError(el.tag + ' is nil, but not expecting nil value')
                elif 'type' in tag_map:
                    value = self._parse_value_as_type(el.text, tag_map['type'])
                else:
                    value = Model.load(self, el)

                lst.append(value)
                logger.debug('Appended ' + str(value) + ' to ' + name)

            elif 'append' in tag_map:
                lst = getattr(self, tag_map['append'])

                if '{http://www.w3.org/2001/XMLSchema-instance}nil' in el.keys() and el.get('{http://www.w3.org/2001/XMLSchema-instance}nil') == 'true':
                    # check if we can accept nil
                    if 'nillable' in tag_map and tag_map['nillable']:
                        value = None
                    else:
                        raise ValueError(el.tag + ' is nil, but not expecting nil value')
                elif 'type' in tag_map:
                    value = self._parse_value_as_type(el.text, tag_map['type'])
                else:
                    value = Model.load(self, el)

                lst.append(value)
                logger.debug('Appended ' + str(value) + ' to ' + tag_map['append'])

            elif 'map' in tag_map:
                dic = getattr(self, tag_map['map'])

                if 'key' in tag_map:
                    try:
                        key = el.get(tag_map['key'])
                    except KeyError:
                        key = None
                # TODO: implement keyElement as well
                else:
                    key = el.get('id')
                    if key is None:
                        raise ValueError('Unable to determine key name for map ' + tag_map['map'] + ' in ' + self.__class__.__name__)

                if '{http://www.w3.org/2001/XMLSchema-instance}nil' in el.keys() and el.get('{http://www.w3.org/2001/XMLSchema-instance}nil') == 'true':
                    # check if we can accept nil
                    if 'nillable' in tag_map and tag_map['nillable']:
                        value = None
                    else:
                        raise ValueError(el.tag + ' is nil, but not expecting nil value')
                elif 'value' in tag_map:
                    try:
                        if 'type' in tag_map:
                            value = self._parse_value_as_type(value, tag_map['type'])
                        else:
                            value = el.get(tag_map['value'])
                    except KeyError:
                        value = None
                # TODO: implement valueElement? as well
                else:
                    if 'type' in tag_map:
                        value = self._parse_value_as_type(el.text, tag_map['type'])
                    else:
                        value = Model.load(self, el)

                dic[key] = value
                logger.debug('Mapped ' + str(key) + ' to ' + str(value) + ' in ' + tag_map['map'])

            elif 'class' in tag_map:
                if '{http://www.w3.org/2001/XMLSchema-instance}nil' in el.keys() and el.get('{http://www.w3.org/2001/XMLSchema-instance}nil') == 'true':
                    # check if we can accept nil
                    if 'nillable' in tag_map and tag_map['nillable']:
                        value = None
                    else:
                        raise ValueError(el.tag + ' is nil, but not expecting nil value')
                else:
                    value = Model.load(self, el)

                if 'in' in tag_map:
                    name = tag_map['in']
                else:
                    name = tag_name.replace('-', '_')

                setattr(self, name, value)
                logger.debug('Set attribute ' + str(name) + ' to ' + str(value) + ' in ' + str(self))

            elif 'type' in tag_map:
                if '{http://www.w3.org/2001/XMLSchema-instance}nil' in el.keys() and el.get('{http://www.w3.org/2001/XMLSchema-instance}nil') == 'true':
                    # check if we can accept nil
                    if 'nillable' in tag_map and tag_map['nillable']:
                        value = None
                    else:
                        raise ValueError(el.tag + ' is nil, but not expecting nil value')
                else:
                    value = self._parse_value_as_type(el.text, tag_map['type'])

                if 'in' in tag_map:
                    name = tag_map['in']
                else:
                    name = tag_name.replace('-', '_')

                setattr(self, name, value)
                logger.debug('Set attribute ' + str(name) + ' to ' + str(value) + ' in ' + str(self))

            elif 'enum' in tag_map:
                if el.text not in tag_map['enum']:
                    raise ValueError(tag + ' value must be one of ' + str(tag_map['enum']))

                if 'in' in tag_map:
                    name = tag_map['in']
                else:
                    name = tag_name.replace('-', '_')

                value = el.text

                setattr(self, name, value)
                logger.debug('Set enum attribute ' + str(name) + ' to ' + str(value) + ' in ' + str(self))

            else:
                return False
            return True

        return False

    def to_xml(self):
        el = ET.Element(self.get_tag())

        for name in self.model_map['attributes']:
            value = self.produce_attribute(name, el)

        for tag in self.model_map['elements']:
            el.extend(self.produce_sub_elements(tag))

        return el

    def produce_attribute(self, name, el):
        if name.endswith('*'):
            return

        xml_namespace, attr_name = Model.parse_tag(name)
        attr_map = self.model_map['attributes'][name]

        if 'notImplemented' in attr_map and attr_map['notImplemented']:
            raise NotImplementedError(name + ' attribute support is not implemented')

        if 'in' in attr_map:
            attr_name = attr_map['in']
        else:
            attr_name = attr_name.replace('-', '_')

        try:
            value = getattr(self, attr_name)
        except AttributeError:
            if 'required' in attr_map and attr_map['required']:
                logger.critical(self.__class__.__name__ + ' must assign required attribute ' + attr_name)
                sys.exit()
            else:
                logger.debug('Skipping attribute ' + attr_name)
                return

        if value is None:
            if 'required' in attr_map and attr_map['required']:
                logger.critical(self.__class__.__name__ + ' must assign required attribute ' + attr_name)
                sys.exit()
            else:
                logger.debug('Skipping attribute ' + attr_name)
                return

        if 'class' in attr_map:
            if not isinstance(value, Model):
                raise ValueError('Need a subclass of Model to set attribute ' + attr_name + ' on ' + self.get_tag() + '; got ' + str(value))

            logger.debug('Setting attribute ' + attr_name + ' on ' + self.get_tag() + ' to ' + value.__class__.__name__ + ' value ' + value.to_string())
            el.set(attr_name, value.to_string())
        elif 'type' in attr_map:
            # TODO nillable
            # if '{http://www.w3.org/2001/XMLSchema-instance}nil' in el.keys() and el.get('{http://www.w3.org/2001/XMLSchema-instance}nil') == 'true':
            #     # check if we can accept nil
            #     if 'nillable' in tag_map and tag_map['nillable']:
            #         value = None
            #     else:
            #         raise ValueError(el.tag + ' is nil, but not expecting nil value')
            logger.debug('Parsing ' + str(value) + ' as ' + attr_map['type'] + ' type')
            v = self._parse_value_as_type(value, attr_map['type'])

            el.set(attr_name, v)
        elif 'enum' in attr_map:
            if value not in attr_map['enum']:
                raise ValueError(name + ' attribute must be one of ' + str(attr_map['enum']) + ': ' + str(value))
            el.set(attr_name, value)
        else:
            raise ValueError('Unable to produce attribute ' + attr_name + '; no class, type or enum definition')

    def produce_sub_elements(self, tag):
        sub_els = []
        if tag.endswith('*'):
            return []

        xml_namespace, tag_name = Model.parse_tag(tag)
        tag_map = self.model_map['elements'][tag]
        if 'append' in tag_map:
            lst = getattr(self, tag_map['append'])
            logger.debug('Appending ' + tag + ' elements from append ' + tag_map['append'])

            # check minimum tag count
            if 'min' in tag_map and tag_map['min'] > len(lst):
                logger.critical(self.__class__.__name__ + ' must have at least ' + tag_map['min'] + ' ' + tag + ' elements')
                sys.exit()
            # check maximum tag count
            if 'max' in tag_map and tag_map['max'] is not None and tag_map['max'] <= len(lst):
                logger.critical(self.__class__.__name__ + ' must have at most ' + tag_map['max'] + ' ' + tag + ' elements')
                sys.exit()

            for i in lst:
                if 'class' in tag_map or 'type' in tag_map:
                    if isinstance(i, Model):
                        sub_els.append(i.to_xml())
                    elif isinstance(i, ET.Element):
                        sub_els.append(i)
                    else:
                        raise ValueError('Unknown class to add to sub elemetns: ' + i.__class__.__name__)
                else:
                    el = ET.Element(tag)
                    el.text = i
                    sub_els.append(el)
        elif 'map' in tag_map:
            dic = getattr(self, tag_map['map'])
            logger.debug('Appending ' + tag + ' elements from map ' + tag_map['map'])

            # check minimum tag count
            if 'min' in tag_map and tag_map['min'] > len(dic):
                logger.critical(self.__class__.__name__ + ' must have at least ' + tag_map['min'] + ' ' + tag + ' elements')
                sys.exit()

            # check maximum tag count
            if 'max' in tag_map and tag_map['max'] is not None and tag_map['max'] <= len(dic):
                logger.critical(self.__class__.__name__ + ' must have at most ' + tag_map['max'] + ' ' + tag + ' elements')
                sys.exit()

            if 'key' in tag_map:
                key_name = tag_map['key']
            else:
                key_name = 'id'
            for k,v in list(dic.items()):
                if 'class' in tag_map:
                    sub_els.append(v.to_xml())
                elif 'type' in tag_map:
                    sub_els.append()
                else:
                    el = ET.Element(tag)
                    el.set(key_name, k)

                    if 'value' in tag_map:
                        value_name = tag_map['value']
                        el.set(value_name, v)
                    else:
                        el.text = v
                    sub_els.append(el)

        elif 'class' in tag_map or 'type' in tag_map or 'enum' in tag_map:
            if 'in' in tag_map:
                name = tag_map['in']
            else:
                name = tag_name.replace('-', '_')

            value = getattr(self, name)
            if value is None:
                return []

            logger.debug('Appending ' + value.__class__.__name__ + ' to ' + self.get_tag())
            if isinstance(value, Model):
                sub_els.append(value.to_xml())
            elif isinstance(value, ET.Element):
                sub_els.append(value)
            else:
                raise ValueError('Unknown class to add to sub elemetns: ' + i.__class__.__name__)

        return sub_els

    def is_reference(self, ref):
        if hasattr(self, 'id') and self.id == ref:
            return True
        return False

    def find_reference(self, ref):
        for _class in Model.index:
            if ref in Model.index[_class]:
                return Model.index[_class][ref]

        # last ditch attempt, try the content_cache
        return Model.find_content(ref)
