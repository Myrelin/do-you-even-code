import logging
import threading
import time

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
#config file, json
#toml
#yaml


class ProcessChecker(threading.Thread):
    def __init__(self, process_names):
        if not HAS_PSUTIL:
            logger.warning("Please install psutil: pip install psutil")
        if not HAS_RUNTIME_TRACKER:
            logger.warning("Please make sure the runtime tracker is in the modules directory!")
        else:
            self.process_names = process_names
            self.running_processes = self.check_if_process_running()
            self.list_of_running_process_objects = self.get_process_id_by_name()
            self.list_of_terminated_processes = self.check_if_process_terminated()


    def check_if_process_running(self):
        running_processes = map(lambda item: item.name(), psutil.process_iter())
        return list(set(self.process_names).intersection(running_processes))

    def check_if_process_terminated(self):
        terminated_process_pids = []
        for pid in self.list_of_running_process_objects:
            if not psutil.pid_exists(pid.get('pid')):
                terminated_process_pids.append(pid.get('pid'))
        return terminated_process_pids



    def get_process_id_by_name(self):
        list_of_process_objects = []
        for process_name in self.running_processes:
            for proc in psutil.process_iter():
                try:
                    process_info = proc.as_dict(attrs=['pid', 'name', 'create_time'])
                    if process_name.lower() in process_info['name'].lower():
                        list_of_process_objects.append(process_info)
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
        print(list_of_process_objects)
        return list_of_process_objects

    def __repr__(self):
        return str(self.__dict__)
