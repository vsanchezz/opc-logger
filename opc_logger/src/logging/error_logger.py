import logging
from datetime import datetime

class ErrorLogger:
    def __init__(self, log_file='./data/logs/error_log.txt'):
        self.log_file = log_file
        self._setup_logger()

    def _setup_logger(self):
        pass

    def log_error(self, message, exception=None):
        pass

    def log_info(self, message):
        pass
