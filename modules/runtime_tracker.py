class ProcessRunTimeTracker:

    def __init__(self, process_name, process_id, start_time):
        self.process_name = process_name
        self.process_id = process_id
        self.start_time = start_time
        self.finish_time = 0
        self.total_time = 0
        self.is_session_closed = False
        time.time

    def __repr__(self):
        return str(self.__dict__)

    def end_session(self, end_time):
        self.finish_time = end_time
        self.is_session_closed = True

    def set_session_total_time(self):
        total_time = self.finish_time - self.start_time
        if total_time > 3600:
            hours = total_time // 3600
            remainder_in_minutes = total_time % 3600
            if remainder_in_minutes > 60:
                minutes = remainder_in_minutes // 60
                seconds = remainder_in_minutes % 60
                self.total_time = "{}:{}:{}".format(hours, minutes, seconds)
        elif 60 < total_time < 3600:
            minutes = total_time // 60
            seconds = total_time % 60
            self.total_time = "0:{}:{}".format(minutes, seconds)
