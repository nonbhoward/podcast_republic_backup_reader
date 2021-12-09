import os
from tool.file_system import get_list_of_backups_from_
from tool.zip_file import get_zipfile_at_

# fetch files
home = os.getenv("HOME")
list_of_backup_files = get_list_of_backups_from_(home)

# TODO more granular archive selection
a_zipfile_path = list_of_backup_files[0]
zip_file = get_zipfile_at_(a_zipfile_path)