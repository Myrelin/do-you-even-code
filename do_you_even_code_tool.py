import importlib
import logging
import time
import os

logger = logging.getLogger('doyouevencode')
process_names = ["pycharm.sh", "idea.sh"]

try:
    from .modules import *
    HAS_PACKAGE_MODULES = True
except Exception as e:
    print(e)
    HAS_PACKAGE_MODULES = False

def main():
    modules = load_modules()
    import sys

    modulename = 'process_checker'
    if modulename not in sys.modules:
        print('You have not imported the {} module'.format(modulename))

    while True:
        for module in modules:
            modules[module].check()
            time.sleep(5)

def load_modules():
    filenames = os.listdir("modules")
    imported_modules = {}
    for file_name in filenames:
        if "__" not in file_name:
            module_name = file_name.split(".")[0]
            module_instance = convert_filename_to_classname(module_name)
            print(module_name, module_instance)
            # imported_modules.update({module_name: convert_filename_to_classname(file_name)})
            try:

                imported_modules[module_name] = __import__('modules.' + module_name)
            except ModuleNotFoundError:
                print("module not found for some fucking reason")
    print(imported_modules)
    return imported_modules


def convert_filename_to_classname(file_name):
    if "_" in str(file_name):
        name_list = file_name.split("_")
        # name_list[-1] = name_list[-1].split(".")[0]
        for i in range(len(name_list)):
            name_list[i] = name_list[i].capitalize()
        return "".join(name_list)


if __name__ == '__main__':
    main()
