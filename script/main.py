import logging
from tool.log_config import configure_logger
from tool.podcast_data import PodcastRepublicBackupData
from tool.zip_archive import extract_details_from_
from tool.zip_archive import get_zip_archives
configure_logger()
log = logging.getLogger()  # root
zip_archives = get_zip_archives()
zip_archive_details = extract_details_from_(zip_archives, decompress=True)
podcast_republic_backup = PodcastRepublicBackupData(zip_archive_details)
pass
