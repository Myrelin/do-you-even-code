import logging
import time
import data_manager

logger = logging.getLogger('doyouevencode')
process_names = ["pycharm.sh", "idea.sh"]

try:
    from modules import process_checker
    HAS_PROCESS_CHECKER = True
except ImportError:
    HAS_PROCESS_CHECKER = False


class DoYouEvenCodeTool:
    def __init__(self):
        if not HAS_PROCESS_CHECKER:
            logger.warning('Please make sure the process_checker is in the modules directory!')
        else:
            self.process_check = process_checker.ProcessChecker(process_names)
            self.create_runtime_trackers()

    def create_runtime_trackers(self):
        running_process_objects = self.process_check.list_of_running_process_objects
        for proc in running_process_objects:
            print(proc)
            if data_manager.get_session_by_pid(proc['pid']) is None:
                data_manager.add_coding_session(proc['name'],
                                                proc['pid'],
                                                proc['create_time'])

                print("new session added to db!")
            else:
                data_manager.update_last_modified_time(proc['pid'], time.time())
                print(data_manager.get_session_by_pid(proc['pid']))

def main():
    while True:

        DoYouEvenCodeTool()
        time.sleep(5)


if __name__ == '__main__':
    main()
