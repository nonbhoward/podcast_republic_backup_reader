import logging
import os
import pathlib
log = logging.getLogger(__name__)


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
