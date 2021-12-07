import logging
from constant.logging_strings import log_filename
from constant.logging_strings import log_filemode
from constant.logging_strings import log_format
log = logging.getLogger(__name__)


def configure_logger():
    logging.basicConfig(filename=log_filename,
                        filemode=log_filemode,
                        format=log_format,
                        level=logging.DEBUG)
    log.debug('logger configured')
