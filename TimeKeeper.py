import ProcessChecker
import threading


class TimeKeeper:
    def __init__(self):
        self.process_checker = threading.Timer(10.0, ProcessChecker.check_if_process_running("pycharm.sh"))

    def cancel_timer(self):
        if not ProcessChecker.check_if_process_running("pycharm.sh"):
            self.process_checker.cancel()


test_time_keeper = TimeKeeper()
print(test_time_keeper)

# self._ == protected
# self.__ == private


#New classes inherited from Thread
#run method override