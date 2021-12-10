import logging
from tool.log_config import configure_logger
from tool.zip_archive import get_zip_archives
configure_logger()
log = logging.getLogger()  # root
zip_archives = get_zip_archives()
# zip_archive_details = extract_details_from_(zip_archives)
# host_on_local_port_(zip_archive_details)
