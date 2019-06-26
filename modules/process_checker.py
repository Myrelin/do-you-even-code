import logging
import threading
import time

try:
    import psutil
    HAS_PSUTIL = True
except ImportError:
    HAS_PSUTIL = False

logger = logging.getLogger('doyouevencode')

process_names = ["pycharm.sh", "idea.sh"]


def check_if_process_running():
    # processes = map(lambda item: item.name(), psutil.process_iter())
    # running = list(filter(lambda item_name: item_name in processes, process_names))
    # print(running)
    # return running


def find_process_id_by_name(process_name):
    list_of_process_objects = []
    for proc in psutil.process_iter():
        try:
            process_info = proc.as_dict(attrs=['pid', 'name', 'create_time'])
            if process_name.lower() in process_info['name'].lower():
                list_of_process_objects.append(process_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    print(list_of_process_objects)
    return list_of_process_objects


class ProcessChecker(threading.Thread):
    def __init__(self):
        if not HAS_PSUTIL:
            logger.warning("Please install psutil: pip install psutil")
        else:
            threading.Thread.__init__(self)
            self.running_processes = check_if_process_running()
            time.sleep(5)
