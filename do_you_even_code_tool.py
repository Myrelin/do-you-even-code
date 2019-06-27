import logging
import os

#
# logger = logging.getLogger('doyouevencode')
#
# process_names = ["pycharm.sh", "idea.sh"]
#
# try:
#     from modules import process_checker
#     HAS_PROCESS_CHECKER = True
# except ImportError:
#     HAS_PROCESS_CHECKER = False
#
#
# class DoYouEvenCodeTool:
#     def __init__(self):
#         if not HAS_PROCESS_CHECKER:
#             logger.warning('Please make sure the process_checker is in the modules directory!')
#

def main():
    modules = load_modules()
    while True:
        for module in modules:
            modules[module].check()
        pass


def load_modules():
    modules = {}
    for filename in os.listdir("/home/myrelin/codecool/pet_projects/do-you-even-code/modules"):
        module_name = convert_to_class_name(filename)
        try:
            __import__(module_name)
            modules[module_name] = module_name()
            modules.update(module_name)
        except ImportError:
            pass
    print(modules)
    return modules


def convert_to_class_name(filename):
    try:
        fileparts = filename.split(".")
        print(filename)
        return fileparts[0]
    except "." not in filename:
        pass





#
#
#
#
#
#
#
#
#
#
#
# import logging
# import time
#
# import data_manager
#
#
#
#
#
#
#     def save_running_processes(self):
#         running_process_objects = self.process_check.list_of_running_process_objects
#         for proc in running_process_objects:
#             if data_manager.get_session_by_pid(proc['pid']) is None:
#                 new_process = proc.as_dict(proc['name'], proc['pid'], proc['create_time'])
#                 data_manager.add_coding_session(new_process.process_name,
#                                                 new_process.process_id,
#                                                 new_process.start_time,
#                                                 new_process.start_time)
#                 print("new session added to db!")
#             else:
#                 process = data_manager.get_session_by_pid(proc['pid'])
#                 print(process)
#                 print("This session has already been logged in the db!")
#
# def main():
#     while True:
#         DoYouEvenCodeTool()
#

if __name__ == '__main__':
    main()
