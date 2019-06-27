import time


class ProcessRunTimeTracker:

    def __init__(self, process_name, process_id, start_time):
        self.process_name = process_name
        self.process_id = process_id
        self.start_time = start_time
        self.finish_time = 0
        self.total_time = 0
        self.is_session_closed = False

    def __repr__(self):
        return str(self.__dict__)
