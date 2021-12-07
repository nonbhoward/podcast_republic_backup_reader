import os
from tool.file_system_ops import get_list_of_backups_from_
from tool.zip_file_ops import get_zipfile_at_
home = os.getenv("HOME")
list_of_backup_files = get_list_of_backups_from_(home)
# TODO more granular archive selection
a_zipfile_path = list_of_backup_files[0]
zip_file = get_zipfile_at_(a_zipfile_path)
pass
