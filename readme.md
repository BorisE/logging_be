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
from logging_be import init_logging, logger
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
## Example
```python
import logging
from logging_be import init_logging, logger

init_logging(console_log_level = logging.INFO, log_path="log")

logger.action("This is an action message.")  // in green
logger.debug("Debug test")                   // if allowed in console, otherwise only to log files
logger.error("We've got an error")           // in red
```


## License

[MIT](https://choosealicense.com/licenses/mit/)