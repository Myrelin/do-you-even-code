import time


class ProcessRunTimeTracker:

    def __init__(self, process_name, process_id):
        self.process_name = process_name
        self.process_id = process_id
        self.start_time = 0
        self.finish_time = 0
        self.total_time = 0
        self.is_session_closed = False
