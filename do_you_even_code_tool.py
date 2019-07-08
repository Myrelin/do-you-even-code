import importlib
import logging
import sys
import time
import os

logger = logging.getLogger('doyouevencode')
process_names = ["pycharm.sh", "idea.sh"]


def main():
    all_modules = load_modules()
    while True:
        for module_name, import_path in all_modules.items():
            try:
                module_instance = convert_filename_to_classname(module_name)
                getattr(import_path, module_instance)().check()
            except AttributeError:
                logger.warning("No named attribute found for {}!".format(module_name))
                import_path.check()
        time.sleep(5)


def load_modules():
    filenames = os.listdir("modules")
    imported_modules = {}
    for file_name in filenames:
        if "__" not in file_name:
            module_name = file_name.split(".")[0]

            try:
                imported_modules[module_name] = importlib.import_module('modules.' + module_name)
            except ModuleNotFoundError:
                print("module not found for some fucking reason")
    sys.modules.update(imported_modules)
    return imported_modules


def convert_filename_to_classname(file_name):
    if "_" in str(file_name):
        name_list = file_name.split("_")
        for i in range(len(name_list)):
            name_list[i] = name_list[i].capitalize()
        return "".join(name_list)


if __name__ == '__main__':
    main()
