import logging
import os
import zipfile
from tool.file_system import get_list_of_backups_from_
from tool.file_system import get_path_home
from tool.file_system import get_zipfile_at_
from tool.file_system import get_file_data_for_
log = logging.getLogger(__name__)


def extract_details_from_(zip_archives, decompress=False):
    archive_details = dict()
    for zip_archive in zip_archives:
        path_to_archive = get_path_to_(zip_archive)
        for file in zip_archive.filelist:
            file_details = get_details_from_(file)
            file_details.update({
                'parent': zip_archive,
                'path to archive': path_to_archive
            })
            archive_details.update({
                (path_to_archive, file.filename): file_details
            })
            if decompress:
                with zipfile.ZipFile(path_to_archive, 'r') as zip_file:
                    decompressed_file = zip_file.extract(member=file)
                with open(decompressed_file, 'r') as dzip_file:
                    file_data = get_file_data_for_(dzip_file.name)
                archive_details[(path_to_archive, file.filename)].update({
                    'file_data': file_data
                })
                delete_(decompressed_file)
    return archive_details


def get_zip_archives() -> list:
    """
    :return: list of zipfile
    """
    home = get_path_home()
    backup_files = get_list_of_backups_from_(home)
    if not backup_files:
        print(f'no backup files found')
    zip_archives = []
    for backup_file in backup_files:
        zip_archives.append(get_zipfile_at_(backup_file))
    return zip_archives


def get_path_to_(zip_archive):
    """
    :param zip_archive: a zipfile
    :return: a / delimited path string
    """
    return zip_archive.filename


def get_details_from_(file):
    file_details = {
        'crc': file.CRC,
        'compress_size': file.compress_size,
        'file_size': file.file_size,
        'filename': file.filename,
        'flag_bits': file.flag_bits,
    }
    return file_details


def delete_(decompressed_file):
    try:
        os.remove(decompressed_file)
    except Exception as exc:
        log.exception(f'failed to remove file')
        for arg in exc.args[0]:
            log.exception(f'{arg}')
