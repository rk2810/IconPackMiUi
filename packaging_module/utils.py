import subprocess
import os
import shutil


def get_icon_res_path():
    return os.getcwd() + "res/icon_pack_res"


def check_unzip_available():
    try:
        subprocess.run(["unzip", "-v"])
    except FileNotFoundError:
        raise Exception("Please install unzip on your machine to continue.")

    return True


def check_if_file_path_exists(file_path):
    try:
        os.stat(file_path)
    except FileNotFoundError:
        raise Exception("Please provide exact/absolute path of icon pack")


def shred_icon_pack_apk_res():
    current_dir = os.getcwd()
    icon_res_dir = current_dir + "/res/icon_pack_res"
    try:
        shutil.rmtree(icon_res_dir)
    except FileNotFoundError:
        pass


def unzip_apk(file_path):
    """will unpack zip to a particular location always and make sure its empty always"""
    shred_icon_pack_apk_res()
    check_if_file_path_exists(file_path)
    icon_res_path = get_icon_res_path()
    subprocess.run(["subprocess", file_path, "-d", icon_res_path])


def get_app_filter_xml_path():
    return os.getcwd() + "/res/icon_pack_res"
