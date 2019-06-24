import psutil
import threading
import time

process_names = ["pycharm.sh", "idea.sh"]


def check_if_process_running():
    processes = map(lambda item: item.name(), psutil.process_iter())
    running = list(filter(lambda item_name: item_name in processes, process_names))
    print(running)


class ProcessChecker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.is_ide_open = False
        check_if_process_running()
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
        if not self.process_checker.is_ide_open and check_if_process_running():
            self.start_time = time.time()
            print("This is the start time! {}".format(self.start_time))
            self.process_checker.is_ide_open = True
            return self.start_time

        elif self.process_checker.is_ide_open and not check_if_process_running():
            self.stop_time = time.time()
            print("This is the stop time! {}".format(self.stop_time))
            self.process_checker.is_ide_open = False
            if self.start_time != 0 and self.stop_time != 0:
                self.total_time = self.stop_time - self.start_time
                print("THIS IS THE TOTAL TIMESIE {}".format(self.total_time))


def main():
    while True:
        process_checker = ProcessChecker()
        code_timekeeper = CodeTimer(process_checker)
#        process_checker.start()
        code_timekeeper.start()


if __name__ == '__main__':
    main()
