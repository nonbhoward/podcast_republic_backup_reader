import logging
import zipfile
from tool.file_system import get_list_of_backups_from_
from tool.file_system import get_parent_of_
from tool.file_system import get_path_home
from tool.file_system import get_zipfile_at_
log = logging.getLogger(__name__)


def extract_details_from_(zip_archives, decompress=False):
    archive_details = dict()
    for zip_archive in zip_archives:
        path_to_archive = get_path_to_(zip_archive)
        path_to_archives = get_parent_of_(path_to_archive)
        for file in zip_archive.filelist:
            file_details = {
                'crc': file.CRC,
                'compress_size': file.compress_size,
                'file_size': file.file_size,
                'filename': file.filename,
                'flag_bits': file.flag_bits,
                'parent': zip_archive,
                'path to archive': path_to_archive
            }
            archive_details.update({
                (path_to_archive, file.filename): file_details
            })
            if decompress:
                with zipfile.ZipFile(path_to_archive, 'r') as zip_file:
                    decompressed_file = zip_file.extract(member=file)
                with open(decompressed_file, 'r') as dzip_file:
                    contents = dzip_file.read()
                    pass
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
