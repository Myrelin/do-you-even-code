import time


class ProcessRunTimeTracker():
    def __init__(self, process_name):
        self.process_name = process_name
        self.start_time = 0
        self.stop_time = 0
        self.total_time = 0


    def code_timer(self, process_name):
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
