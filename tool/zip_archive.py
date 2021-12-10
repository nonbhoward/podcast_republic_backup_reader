import logging
from tool.file_system import get_list_of_backups_from_
from tool.file_system import get_path_home
from tool.file_system import get_zipfile_at_
log = logging.getLogger(__name__)


def get_zip_archives():
    home = get_path_home()
    backup_files = get_list_of_backups_from_(home)
    if not backup_files:
        print(f'no backup files found')
    zip_archives = []
    for backup_file in backup_files:
        zip_archives.append(get_zipfile_at_(backup_file))
    return zip_archives
