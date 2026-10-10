import logging
import os
from logging.handlers import RotatingFileHandler
def setup_logger(name = "ops_auto", log_file = "/var/log/ops/automation.log",level = logging.DEBUG):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if logger.hasHandlers():
        return logger
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    file_handler = RotatingFileHandler(log_file, maxBytes=10*1024*1024, backupCount=5)
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)-8s | %(message)s")
    console.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    logger.addHandler(console)
    logger.addHandler(file_handler)
    return logger