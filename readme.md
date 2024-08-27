# Custom logging package

**logging_be** is a custom Python library for customized logging, wrapped on **logging** package.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install **logging_be**.

```bash
pip install logging     # default logging package
pip install logging_be  # customized wrapper
```
## Usage
To import, use:
```python
import logging
import logging_be 
from logging_be import logger
```
or simpler:
```python
from logging_be import *
```
then call **init_logging()**
```python
init_logging(
    console_log_level = logging.INFO, 
    log_path = "",
    info_log_filename = f"info_log_{time.strftime('%Y%m%d_%H%M%S')}.log", 
    debug_log_filename = f"debug_log_{time.strftime('%Y%m%d_%H%M%S')}.log", 
    error_log_filename = f"error_log_{time.strftime('%Y%m%d_%H%M%S')}.log", 
    file_log_format = "%(asctime)s [%(levelname)-6s] %(module)s/%(funcName)-15s: %(message)s",
    console_log_format = "%(funcName)-8s: %(message)s"
)
```
* from 1.0.3 default parameters for filename if None
## Example
```python
import logging
from logging_be import init_logging, logger

init_logging(console_log_level = logging.INFO, log_path="log")

logger.action("This is an action message.")  // in green
logger.debug("Debug test")                   // if allowed in console, otherwise only to log files
logger.error("We've got an error")           // in red
```
## Possible formaters
https://docs.python.org/3/library/logging.html#logrecord-attributes

|Attribute name|Format|Description|
| ------------- | --- | --- |
|args|You shouldn’t need to format this yourself.|The tuple of arguments merged into msg to produce message, or a dict whose values are used for the merge (when there is only one argument, and it is a dictionary)|
|asctime|%(asctime)s|Human-readable time when the LogRecord was created. By default this is of the form ‘2003-07-08 16:49:45,896’ (the numbers after the comma are millisecond portion of the time).|
|created|%(created)f|Time when the LogRecord was created (as returned by time.time()).|
|exc_info|You shouldn’t need to format this yourself.|Exception tuple (à la sys.exc_info) or, if no exception has occurred, None.
|filename|%(filename)s|Filename portion of pathname.
|funcName|%(funcName)s|Name of function containing the logging call.
|levelname|%(levelname)s|Text logging level for the message ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
|levelno|%(levelno)s|Numeric logging level for the message (DEBUG, INFO, WARNING, ERROR, CRITICAL).
|lineno|%(lineno)d|Source line number where the logging call was issued (if available).
|message|%(message)s|The logged message, computed as msg % args. This is set when Formatter.format() is invoked.
|module|%(module)s|Module (name portion of filename).
|msecs|%(msecs)d|Millisecond portion of the time when the LogRecord was created.
|msg|You shouldn’t need to format this yourself.|The format string passed in the original logging call. Merged with args to produce message, or an arbitrary object (see Using arbitrary objects as messages).
|name|%(name)s|Name of the logger used to log the call.
|pathname|%(pathname)s|Full pathname of the source file where the logging call was issued (if available).
|process|%(process)d|Process ID (if available).
|processName|%(processName)s|Process name (if available).
|relativeCreated|%(relativeCreated)d|Time in milliseconds when the LogRecord was created, relative to the time the logging module was loaded.
|stack_info|You shouldn’t need to format this yourself.|Stack frame information (where available) from the bottom of the stack in the current thread, up to and including the stack frame of the logging call which resulted in the creation of this record.
|thread|%(thread)d|Thread ID (if available).
|threadName|%(threadName)s|Thread name (if available).
|taskName|%(taskName)s|asyncio.Task name (if available).

## License

[MIT](https://choosealicense.com/licenses/mit/)