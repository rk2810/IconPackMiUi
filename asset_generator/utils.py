from xml.etree import ElementTree


def cleanse_name(name):
    new_name = name.replace("ComponentInfo{", "")
    new_name = new_name.replace("}", "")
    return new_name


def get_app_filter_xml(xml_path):
    xml_tree = ElementTree.parse(xml_path)
    return xml_tree
