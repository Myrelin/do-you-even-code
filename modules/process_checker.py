import logging
import time

try:
    import psutil
    HAS_PSUTIL = True
except ImportError:
    HAS_PSUTIL = False

try:
    import data_manager
    HAS_DATA_MANAGER = True
except ImportError:
    HAS_DATA_MANAGER = False


logger = logging.getLogger('doyouevencode')
process_names = ["pycharm.sh", "idea.sh", "eclipse"]


def check():
    print("TESTING A THING")


class ProcessChecker:
    def __init__(self):
        if not HAS_PSUTIL:
            logger.warning("Please install psutil: pip install psutil")
        if not HAS_DATA_MANAGER:
            logger.warning("Data manager for query handling missing!")
        else:
            self.process_names = process_names
            time.sleep(3)

    def check_if_process_running(self):
        running_processes = map(lambda item: item.name(), psutil.process_iter())
        return list(set(self.process_names).intersection(running_processes))

    def get_process_id_by_name(self):
        list_of_process_objects = []
        for process_name in self.check_if_process_running():
            for proc in psutil.process_iter():
                try:
                    process_info = proc.as_dict(attrs=['pid', 'name', 'create_time'])
                    if process_name.lower() in process_info['name'].lower():
                        list_of_process_objects.append(process_info)
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
        return list_of_process_objects

    def update_sessions(self):
        for proc in self.get_process_id_by_name():
            if data_manager.get_session_by_pid(proc['pid']) is None:
                data_manager.add_coding_session(proc['name'],
                                                proc['pid'],
                                                proc['create_time'])
                print("new session added to db!")
            else:
                data_manager.update_last_modified_time(proc['pid'], time.time())
                print("running session updated!")

    def close_sessions(self):
        open_sessions = data_manager.get_open_sessions()
        for session in open_sessions:
            if not psutil.pid_exists(session['process_id']):
                data_manager.close_session(session['process_id'])

    def check(self):
        self.check_if_process_running()
        self.get_process_id_by_name()
        self.update_sessions()
        self.close_sessions()

    def __repr__(self):
        return str(self.__dict__)
