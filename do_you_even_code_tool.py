import importlib
import logging
import sys
import time
import os
from modules import *


logger = logging.getLogger('doyouevencode')
process_names = ["pycharm.sh", "idea.sh"]

# try:
#     from modules import *
#     HAS_PACKAGE_MODULES = True
# except Exception as e:
#     print(e)
#     HAS_PACKAGE_MODULES = False

def main():
    all_modules = load_modules()
    while True:
        for module in all_modules:

            all_modules[module].check()
            time.sleep(5)

def load_modules():
    filenames = os.listdir("modules")
    imported_modules = {}
    for file_name in filenames:
        if "__" not in file_name:
            module_name = file_name.split(".")[0]
            module_instance = convert_filename_to_classname(file_name)
            try:
                imported_modules[module_name] = importlib.import_module('modules.' + module_name)
            except ModuleNotFoundError:
                print("module not found for some fucking reason")
    print(imported_modules)
    sys.modules.update(imported_modules)
    return imported_modules



#
# def load_modules(mod_dir):
#     sys.path.append(mod_dir)
#     my_modules = {}
#     for root, dirnames, filenames in os.walk(mod_dir):
#         if os.path.basename(root) == '__pycache':
#             continue
#         if os.path.basename(root).startswith("."):
#             continue
#         for filename in fnmatch.filter(filenames, '*.py'):
#             if root.split('/')[-1].startswith('_'):
#                 continue
#             if filename == '__init.py__':
#                 continue
#             module_name = filename.split(".")[0]
#             try:
#                 my_modules[module_name] = importlib.import_module(os.path.basename(root) + '.' + module_name)
#             except Exception as e:
#                 logger.warning('Tool modules {} failed due to {}'.format(module_name, e))
#     return my_modules



def convert_filename_to_classname(file_name):
    if "_" in str(file_name):
        name_list = file_name.split("_")
        # name_list[-1] = name_list[-1].split(".")[0]
        for i in range(len(name_list)):
            name_list[i] = name_list[i].capitalize()
        return "".join(name_list)


if __name__ == '__main__':
    main()
