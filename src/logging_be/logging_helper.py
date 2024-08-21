'''
Custom logger by Boris Emchenko
v 1.0
2024-08-21


to use it
1) import: 
 import logging
 from logging_be import init_logging, logger
or
 from logging_be import *

2) call init_logging()
    console_log_level = logging.INFO, 
    log_path = "",
    info_log_filename = f"info_log_{time.strftime('%Y%m%d_%H%M%S')}.log", 
    debug_log_filename = f"debug_log_{time.strftime('%Y%m%d_%H%M%S')}.log", 
    error_log_filename = f"error_log_{time.strftime('%Y%m%d_%H%M%S')}.log", 
    file_log_format = "%(asctime)s [%(levelname)-6s] %(module)s/%(funcName)-15s: %(message)s",
    console_log_format = "%(funcName)-8s: %(message)s"


3) use it:
logger.action("This is an action message.") // in green
logger.debug("Debug test")                  // if allowed in
logger.error("We've got an error")
'''


import sys
import time
import logging

import os
os.system("")

CHEAD = '\033[92m'
CWRONG = '\033[2;31;43m' # red on orrange bg
CRED = '\033[91m'
CYEL = '\033[33m'
CBLUE = '\033[94m'
CPURPLE = '\033[95m'
CDARKCYAN = '\033[36m'
CLIGHTGREY = '\033[37m'
CDARKGREY = '\033[90m'
CBOLD = '\033[1m'
CEND = '\033[0m'


logger = logging.getLogger('custom_logger')


# New level
ACTION_LEVEL_NUM = 25  # Between INFO (20) and WARNING (30)
logging.addLevelName(ACTION_LEVEL_NUM, "ACTION")

def action(self, message, *args, **kwargs):
    if self.isEnabledFor(ACTION_LEVEL_NUM):
        self._log(ACTION_LEVEL_NUM, message, args, **kwargs)

logging.Logger.action = action


# Filter for console handler to exclude WARNING and ERROR levels
class MaxLevelFilter(logging.Filter):
    def __init__(self, level):
        self.max_level = level

    def filter(self, record):
        return record.levelno <= self.max_level


# Console Handler for Error Logs (Red colored)
class ConsoleErrorHandler(logging.StreamHandler):
    def emit(self, record):
        try:
            if record.levelno >= logging.WARNING:
                record.msg = CRED + record.msg + CEND  # Red color
            super().emit(record)
        except Exception:
            self.handleError(record)

# Console Handler for Action Logs (Green colored)
class ConsoleActionHandler(logging.StreamHandler):
    def emit(self, record):
        try:
            if record.levelno == ACTION_LEVEL_NUM:
                record.msg = CHEAD + record.msg + CEND 
            super().emit(record)
        except Exception:
            self.handleError(record)

'''
Call to initialize custom logging
'''
def init_logging(console_log_level = logging.INFO, 
                 log_path = "",
                 info_log_filename = f"info_log_{time.strftime('%Y%m%d_%H%M%S')}.log", 
                 debug_log_filename = f"debug_log_{time.strftime('%Y%m%d_%H%M%S')}.log", 
                 error_log_filename = f"error_log_{time.strftime('%Y%m%d_%H%M%S')}.log", 
                 file_log_format = "%(asctime)s [%(levelname)-6s] %(module)s/%(funcName)-15s: %(message)s",
                 console_log_format = "%(funcName)-8s: %(message)s"
                ):
    global logger
    
    logger.setLevel(logging.DEBUG)

    # Define the handlers for console and file output
    console_handler = logging.StreamHandler()  # Console output
    console_handler.setLevel(console_log_level)
    console_handler.setFormatter(logging.Formatter(console_log_format))
    console_handler.encoding='utf-8'
    console_handler.addFilter(MaxLevelFilter(logging.INFO)) 
    logger.addHandler(console_handler)

    if (info_log_filename) :
        info_file_handler = logging.FileHandler(os.path.join(log_path, info_log_filename))  # File output
        info_file_handler.setLevel(logging.INFO)
        info_file_handler.setFormatter(logging.Formatter(file_log_format))
        info_file_handler.encoding='utf-8'
        logger.addHandler(info_file_handler)

    if (debug_log_filename):
        debug_file_handler = logging.FileHandler(os.path.join(log_path, debug_log_filename))
        debug_file_handler.setLevel(logging.DEBUG)
        debug_file_handler.setFormatter(logging.Formatter(file_log_format))
        debug_file_handler.encoding='utf-8'
        logger.addHandler(debug_file_handler)

    if (error_log_filename):
        error_file_handler = logging.FileHandler(os.path.join(log_path, error_log_filename))
        error_file_handler.setLevel(logging.WARNING)
        error_file_handler.setFormatter(logging.Formatter(file_log_format))
        error_file_handler.encoding='utf-8'
        logger.addHandler(error_file_handler)

    console_action_handler = ConsoleActionHandler(sys.stdout)
    console_action_handler.setLevel(ACTION_LEVEL_NUM)
    console_action_handler.setFormatter(logging.Formatter(console_log_format))
    console_action_handler.addFilter(MaxLevelFilter(ACTION_LEVEL_NUM)) 
    logger.addHandler(console_action_handler)

    console_error_handler = ConsoleErrorHandler(sys.stderr)
    console_error_handler.setLevel(logging.WARNING)
    console_error_handler.setFormatter(logging.Formatter(console_log_format))
    logger.addHandler(console_error_handler)


if __name__ == "__main__":
    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.action("This is an action message.")  # Custom ACTION level
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")