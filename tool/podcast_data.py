import json
import sqlite3


class PodcastRepublicBackupData:
    data = None

    def __init__(self,
                 zip_archive_details):
        self.zip_archive_details = zip_archive_details
