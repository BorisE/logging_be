'''
Custom logger by Boris Emchenko
v 1.0.5 2024-08-31
----------------------------------------------------------------
1.0.5 2024-08-31    - gobal var Debug_Level_Enabled changed to func
1.0.4 2024-08-31    - gobal var Debug_Level_Enabled to check if debug for console enabled
1.0.3 2024-08-27    - changed init_logging file name handling: use Empty string to omit file creation, None or skipping - to use default naming
1.0.2 2024-08-22    - correct unicode support
                    - new func clear_logging() to clear log handlers
                    - tests
1.0.1 2024-08-22    - unicode support
1.0.0 2024-08-19    - inital release
----------------------------------------------------------------
to use it
1) import: 
 import logging
 from logging_be import logger, init_logging
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
    logger.info("Info message.")                // normal message
    logger.action("This is an action message.") // in green
    logger.debug("Debug test")                  // if allowed to be displayed in console
    logger.error("We've got an error")          // in red
----------------------------------------------------------------
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
# https://i.stack.imgur.com/j7e4i.gif
# https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal


# Define main logging object
logger = logging.getLogger('custom_logger')

# Global var to check if debug in console enabled
Debug_Level_Enabled = False

# Define new logging level
ACTION_LEVEL_NUM = 25  # Between INFO (20) and WARNING (30)
logging.addLevelName(ACTION_LEVEL_NUM, "ACTION")

def action(self, message, *args, **kwargs):
    if self.isEnabledFor(ACTION_LEVEL_NUM):
        self._log(ACTION_LEVEL_NUM, message, args, **kwargs)
logging.Logger.action = action


# Filter for console handler to exclude WARNING and ERROR levels
class _MaxLevelFilter(logging.Filter):
    def __init__(self, level):
        self.max_level = level

    def filter(self, record):
        return record.levelno <= self.max_level


# Console Handler for Error Logs (Red colored)
class _ConsoleErrorHandler(logging.StreamHandler):
    def emit(self, record):
        try:
            if record.levelno >= logging.WARNING:
                record.msg = CRED + record.msg + CEND  # Red color
            super().emit(record)
        except Exception:
            self.handleError(record)

# Console Handler for Action Logs (Green colored)
class _ConsoleActionHandler(logging.StreamHandler):
    def emit(self, record):
        try:
            if record.levelno == ACTION_LEVEL_NUM:
                record.msg = CHEAD + record.msg + CEND 
            super().emit(record)
        except Exception:
            self.handleError(record)

def init_logging(console_log_level = logging.INFO, 
                 log_path = "",
                 info_log_filename = None, 
                 debug_log_filename = None, 
                 error_log_filename = None, 
                 file_log_format = "%(asctime)s [%(levelname)-6s] %(module)s/%(funcName)-15s: %(message)s",
                 console_log_format = "%(funcName)-8s: %(message)s"
                ):
    ''' Need to be called to initialize custom logging before using logger.info() and etc
    
    Keyword argument:
        info_log_filename = f"info_log_{time.strftime('%Y%m%d_%H%M%S')}.log"    if info_log_filename is None else info_log_filename 
        debug_log_filename = f"debug_log_{time.strftime('%Y%m%d_%H%M%S')}.log"  if debug_log_filename is None else debug_log_filename 
        error_log_filename = f"error_log_{time.strftime('%Y%m%d_%H%M%S')}.log"  if error_log_filename is None else error_log_filename 
        if empty string, than no log files are created
    '''
    global logger
    global Debug_Level_Enabled
    
    logger.setLevel(logging.DEBUG)

    # Define the handlers for console and file output
    console_handler = logging.StreamHandler()  # Console output
    console_handler.setLevel(console_log_level)
    console_handler.setFormatter(logging.Formatter(console_log_format))
    console_handler.encoding='UTF-8'
    console_handler.addFilter(_MaxLevelFilter(logging.INFO)) 
    logger.addHandler(console_handler)
    
    Debug_Level_Enabled = True if console_log_level == logging.DEBUG else False

    info_log_filename = f"info_log_{time.strftime('%Y%m%d_%H%M%S')}.log"    if info_log_filename is None else info_log_filename 
    debug_log_filename = f"debug_log_{time.strftime('%Y%m%d_%H%M%S')}.log"  if debug_log_filename is None else debug_log_filename 
    error_log_filename = f"error_log_{time.strftime('%Y%m%d_%H%M%S')}.log"  if error_log_filename is None else error_log_filename 

    if (info_log_filename):
        info_file_handler = logging.FileHandler(os.path.join(log_path, info_log_filename), encoding = "UTF-8")  # File output
        info_file_handler.setLevel(logging.INFO)
        info_file_handler.encoding='UTF-8'
        info_file_handler.setFormatter(logging.Formatter(file_log_format))
        logger.addHandler(info_file_handler)

    if (debug_log_filename):
        debug_file_handler = logging.FileHandler(os.path.join(log_path, debug_log_filename), encoding = "UTF-8")
        debug_file_handler.setLevel(logging.DEBUG)
        debug_file_handler.encoding='UTF-8'
        debug_file_handler.setFormatter(logging.Formatter(file_log_format))
        logger.addHandler(debug_file_handler)

    if (error_log_filename):
        error_file_handler = logging.FileHandler(os.path.join(log_path, error_log_filename), encoding = "UTF-8")
        error_file_handler.setLevel(logging.WARNING)
        error_file_handler.encoding='UTF-8'
        error_file_handler.setFormatter(logging.Formatter(file_log_format))
        logger.addHandler(error_file_handler)

    console_action_handler = _ConsoleActionHandler(sys.stdout)
    console_action_handler.setLevel(ACTION_LEVEL_NUM)
    console_action_handler.encoding='UTF-8'
    console_action_handler.setFormatter(logging.Formatter(console_log_format))
    console_action_handler.addFilter(_MaxLevelFilter(ACTION_LEVEL_NUM)) 
    logger.addHandler(console_action_handler)

    console_error_handler = _ConsoleErrorHandler(sys.stderr)
    console_error_handler.setLevel(logging.WARNING)
    console_error_handler.setFormatter(logging.Formatter(console_log_format))
    console_error_handler.encoding='UTF-8'
    logger.addHandler(console_error_handler)

def clear_logging():
    '''Clear current logger handlers. Useful if you want to reinitialize logging with different parameters'''
    logger.handlers.clear() 


if __name__ == "__main__":
    init_logging(
        console_log_level=logging.INFO, 
        info_log_filename = "", 
        debug_log_filename = "", 
        error_log_filename = ""     
    )

    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.action("This is an action message.")  # Custom ACTION level
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.info("This is unicode: Prà")
    
    
def get_debug_enabled() -> bool:
    '''Return status of debug messages output to console. Call init_logging() to change
    
    True -- debug output to console enabled
    False -- debug output to console disabled
    '''
    global Debug_Level_Enabled
    
    return Debug_Level_Enabled