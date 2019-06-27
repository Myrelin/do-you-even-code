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

try:
    from modules import runtime_tracker
    HAS_RUNTIME_TRACKER = True
except ImportError:
    HAS_RUNTIME_TRACKER = False


class DoYouEvenCodeTool:
    def __init__(self):
        if not HAS_PROCESS_CHECKER:
            logger.warning('Please make sure the process_checker is in the modules directory!')
        if not HAS_RUNTIME_TRACKER:
            logger.warning('Please make sure the runtime tracker is in the modules directory!')
        else:
            self.process_check = process_checker.ProcessChecker(process_names)
            self.runtime_trackers = []
            self.create_runtime_trackers()
            # self.filter_finished_processes()

    def create_runtime_trackers(self):
        running_process_objects = self.process_check.list_of_running_process_objects
        for proc in running_process_objects:
            if data_manager.get_session_by_pid(proc['pid']) is None:
                new_process = runtime_tracker.ProcessRunTimeTracker(proc['name'],
                                                                    proc['pid'],
                                                                    proc['create_time'])

                self.runtime_trackers.append(new_process)
                data_manager.add_coding_session(new_process.process_name,
                                                new_process.process_id,
                                                new_process.start_time)

                print("new session added to db!")
            else:
                print("This session has already been logged in the db!")

    # def filter_finished_processes(self):
    #     for tracker in self.runtime_trackers:
    #         if tracker.process_id in self.process_check.list_of_terminated_processes:
    #             print(tracker.process_id)
    #             print(self.process_check.list_of_terminated_processes)
    #             tracker.end_session(time.time)
    #             tracker.set_session_total_time()
    #             print(tracker)


def main():
    while True:
        code_tool = DoYouEvenCodeTool()
        print(code_tool.runtime_trackers)


if __name__ == '__main__':
    main()
