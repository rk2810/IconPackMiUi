from logging_module.logger import Logger
from asset_generator.utils import (cleanse_name)

import os
import shutil

logger = Logger.get_logger("copy_assets")


def populate_icon_mapping_data(tree):
    root = tree.getroot()
    final_data = []

    for node in root:
        component_name = node.attrib.get('component')
        drawable = node.attrib.get("drawable")

        if component_name:
            component_sane_data = cleanse_name(component_name)
            component_list = component_sane_data.split("/")
            final_data.append({"component": component_list, "drawable": drawable})
    return final_data


def populate_assets(final_data):
    moved = 0
    skip_array = []

    current_dir = os.getcwd()
    initial_asset_dir = current_dir + "/initial_assets"
    destination_dir = current_dir + "/final_assets"
    for val in final_data:
        file_name = f"{val['drawable']}.png"

        component_list = val["component"]
        for component in component_list:
            new_name = f"{component}.png"
            try:
                logger.info(f"Trying {file_name}")
                src_file = os.path.join(initial_asset_dir, file_name)
                dst_file = os.path.join(destination_dir, file_name)
                new_dest_file = os.path.join(destination_dir, new_name)
                if not os.path.isfile(new_dest_file) and new_dest_file not in skip_array:
                    shutil.copy(src_file, destination_dir)
                    os.rename(dst_file, new_dest_file)
                    logger.info("done..")
                    moved += 1
                else:
                    skip_array.append(new_dest_file)
                    os.remove(new_dest_file)
                    logger.info("skipped.")
            except Exception as e:
                logger.info(f"Failed with {file_name}")
                logger.info(f"Reason: {e}")
                pass



