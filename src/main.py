import os
from glob import glob
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from gdrive_utils import GoogleDriveOps
from data_collection import ScrapeTweets


def get_drive_instance(cred_file_path):
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(cred_file_path)
    drive = GoogleDrive(gauth)
    return drive

# will scrape tweets and store into ../data dir
ScrapeTweets.run_snscrape_twitter_stream_job('nlproc', 500)

# Upload this data to Gdrive location
all_files = glob('../data/*.json')
drive_local_instance = get_drive_instance('google_api_cred.txt')
classObj = GoogleDriveOps(drive_local_instance)
classObj.upload_data_to_gdrive(all_files, 'your_folder_id')





