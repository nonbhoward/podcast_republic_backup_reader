import logging
import os
import zipfile
log = logging.getLogger(__name__)


def get_zipfile_at_(zipfile_path):
    if not os.path.exists(zipfile_path):
        exit_cause = f'file not found at {zipfile_path}'
        log.exception(exit_cause)
        print(f'{exit_cause}')
        exit()
    if not zipfile.is_zipfile(zipfile_path):
        exit_cause = f'file not zipfile at {zipfile_path}'
        log.exception(exit_cause)
        print(f'{exit_cause}')
        exit()
    with zipfile.ZipFile(zipfile_path, 'r') as zip_file:
        return zip_file
