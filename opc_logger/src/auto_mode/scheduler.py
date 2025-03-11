import time
import threading
from datetime import datetime, timedelta

class Scheduler:
    def __init__(self):
        self.scheduled_tasks = []
        self.running = False
        self.thread = None

    def start(self):
        pass

    def stop(self):
        pass

    def add_task(self, task, start_time, end_time, days):
        pass

    def remove_task(self, task_id):
        pass

    def _run(self):
        pass
