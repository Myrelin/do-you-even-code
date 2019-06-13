import psutil
import threading
import time


def check_if_process_running(process_name):
    for proc in psutil.process_iter():
        try:
            if process_name.lower() in proc.name().lower():
                print("Process {} is running".format(process_name))
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    print("Process {} is not running".format(process_name))
    return False


class ProcessChecker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.is_ide_open = False
        check_if_process_running("idea.sh")
        time.sleep(10)


class CodeTimer(threading.Thread):
    def __init__(self, process_checker):
        threading.Thread.__init__(self)
        self.process_checker = process_checker
        self.start_time = 0
        self.stop_time = 0
        self.total_time = 0
        self.code_timer()

    def code_timer(self):
        if not self.process_checker.is_ide_open and check_if_process_running("idea.sh"):
            self.start_time = time.time()
            print(self.start_time)
            self.process_checker.is_ide_open = True
        elif self.process_checker.is_ide_open and not check_if_process_running("idea.sh"):
            self.stop_time = time.time()
            print(self.stop_time)
            self.process_checker.is_ide_open = False
            self.total_time = self.stop_time - self.start_time
            print("THIS IS THE TOTAL TIMESIE {}".format(self.total_time))


def main():
    while True:
        process_checker = ProcessChecker()
        code_timekeeper = CodeTimer(process_checker)
#        process_checker.start()
        code_timekeeper.start()
        print(code_timekeeper.total_time)


if __name__ == '__main__':
    main()