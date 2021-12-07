import logging
import os
from tool.log_config import configure_logger
configure_logger()
log = logging.getLogger()
home = os.getenv("HOME")
pass
