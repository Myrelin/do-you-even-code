import logging
import threading
import time
import data_manager


try:
    import psutil
    HAS_PSUTIL = True
except ImportError:
    HAS_PSUTIL = False

try:
    from modules import runtime_tracker
    HAS_RUNTIME_TRACKER = True
except ImportError:
    HAS_RUNTIME_TRACKER = False

logger = logging.getLogger('doyouevencode')

process_names = ["pycharm.sh", "idea.sh"]


def check_if_process_running():
    running_processes = map(lambda item:item.name(), psutil.process_iter())
    searched_processes = list(set(process_names).intersection(running_processes))
    return searched_processes


def get_process_id_by_name():
    list_of_process_objects = []
    for process_name in check_if_process_running():
        for proc in psutil.process_iter():
            try:
                process_info = proc.as_dict(attrs=['pid', 'name', 'create_time'])
                if process_name.lower() in process_info['name'].lower():
                    print(process_info['pid'])
                    if data_manager.get_session_by_pid(process_info['pid']) is None:
                        print("not in db yet")
                        list_of_process_objects.append(runtime_tracker.ProcessRunTimeTracker(process_info['name'],
                                                                                             process_info['pid'],
                                                                                             process_info['create_time']))

                        data_manager.add_coding_session(process_info)
                    else:
                        print("This process is already logged in the db")

                    #check db entry by pid and date
                    #if no match, insert new entry
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
    print(list_of_process_objects)
    return list_of_process_objects


class ProcessChecker(threading.Thread):
    def __init__(self):
        if not HAS_PSUTIL:
            logger.warning("Please install psutil: pip install psutil")
        if not HAS_RUNTIME_TRACKER:
            logger.warning("Please make sure the runtime tracker is in the modules directory!")
        else:
            threading.Thread.__init__(self)
            self.running_processes = check_if_process_running()
            get_process_id_by_name()
            time.sleep(5)

    def __repr__(self):
        return str(self.__dict__)
