from packaging_module.utils import (check_unzip_available, unzip_apk, get_app_filter_xml_path)


def unpack_apk(path):
    unzip_available = check_unzip_available()
    if unzip_available:
        unzip_apk(path)
        return get_app_filter_xml_path()
