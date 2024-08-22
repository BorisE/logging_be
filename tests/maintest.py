# from logging_be import *

import logging
from logging_be import init_logging, logger, clear_logging

#logging_be.logging_helper.init_logging(debug_messages=True)

#logging_be.init_logging(debug_messages=True)



def Test_messages():
    logger.action("This is an action message.")  # Custom ACTION level

    logger.info("Info message")

    logger.info("This is unicode info: Prà")
    logger.debug("This is unicode debug: Prà")
    logger.error("This is unicode error: Prà")

    logger.debug("Debug test")
    logger.error("We've got an error")



# w files
print ("*** Test: init logging with files")
init_logging(console_log_level=logging.INFO, 
            log_path='log', 
            console_log_format = "%(message)s",
            file_log_format = "%(asctime)s [%(levelname)-6s] %(module)s/%(funcName)-15s: %(message)s",
            )

Test_messages()

print ("*** clearing previous handlers ***")
clear_logging()

# wo files
print ("*** Test: init logging without files")
init_logging(console_log_level=logging.INFO, 
            info_log_filename = "", 
            debug_log_filename = "", 
            error_log_filename = "",
            console_log_format = "%(message)s",
            file_log_format = "%(asctime)s [%(levelname)-6s] %(module)s/%(funcName)-15s: %(message)s",
            )

Test_messages()

logger.info("Script end")
