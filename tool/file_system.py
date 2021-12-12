import logging
import os
import pathlib
import subprocess
import zipfile
log = logging.getLogger(__name__)


class CommandLine:
    file = 'file'


class Extension:
    recognized = ['zip']


class FilePathName:
    podcast_republic_backups = 'podcast_republic_backups'


def get_list_of_backups_from_(home_dir=''):
    backup_path = get_backup_path_from_(home_dir)
    backup_files = get_backup_files_from_(backup_path)
    if not backup_files:
        exit_cause = f'no backup files found'
        log.exception(exit_cause)
        exit()
    return backup_files


def get_backup_path_from_(home_dir=''):
    if not os.path.exists(home_dir):
        exit_cause = f'path not exist at {home_dir}'
        log.exception(exit_cause)
        print(exit_cause)
        exit()
    backup_path_name = FilePathName.podcast_republic_backups
    backup_path = pathlib.Path(home_dir, backup_path_name)
    if not os.path.exists(backup_path):
        exit_cause = f'path not exist at {backup_path}'
        log.exception(exit_cause)
        print(exit_cause)
        exit()
    log.info(f'returning backup_path as {backup_path}')
    return backup_path


def get_backup_files_from_(backup_path):
    all_files_in_backup_path = list()
    for root, _, files in os.walk(backup_path):
        for file in files:
            all_files_in_backup_path.append(pathlib.Path(root, file))
    backup_files = filter_recognized_files_from_(all_files_in_backup_path)
    return backup_files


def filter_recognized_files_from_(all_files_in_backup_path):
    recognized_files = list()
    for file_in_backup_path in all_files_in_backup_path:
        extension = get_extension_from_(file_in_backup_path)
        if extension in Extension.recognized:
            recognized_files.append(file_in_backup_path)
    return recognized_files


def get_extension_from_(file_in_backup_path):
    if '.' not in str(file_in_backup_path):
        return None
    return str(file_in_backup_path).split('.')[1]


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


def get_path_home():
    home = os.getenv("HOME")
    if not home:
        log.exception(f'no path : {home}')
    return home


def get_parent_of_(path_to_archive):
    parent_path = ''.join([ele + '/' for ele in path_to_archive.split('/')[1:-1]])
    return parent_path


def get_file_data_for_(file_path):
    command = [CommandLine.file, file_path]
    file_data = subprocess.run(args=command, capture_output=True)
    return file_data
