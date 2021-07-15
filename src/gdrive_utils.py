import tqdm
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

class GoogleDriveOps:

    def __init__(self, drive_instance):
        self.drive_instance = drive_instance


    def list_all_gdrive_files(self, drive_folder_id):
        return self.drive_instance.ListFile({'q': "'{}' in parents and trashed=false".format(drive_folder_id)}).GetList()

    
    def create_folder_in_gdrive(self, folder_name):
        try:
            folder = self.drive_instance.CreateFile({'title': folder_name, 'mimeType': 'application/vnd.google-apps.folder'})
            folder.Upload()
            return (True, folder['id'])
        except:
            print('Error in creating folder')
            return (False, None)

    
    def upload_data_to_gdrive(self, list_of_files, drive_folder_id):
        try:
            for file in tqdm.tqdm(list_of_files):
                gfile = self.drive_instance.CreateFile({'parents': [{'id': drive_folder_id}]})
                gfile.SetContentFile(file)
                gfile.Upload()
            return True
        except Exception as e:
            print(e)
            return False


if __name__ == '__main__':
    pass

    #load credentials (First run drive_auth.py, that will verify the credentials and save them to the "google_api_cred.txt" file)
    # gauth = GoogleAuth()
    # gauth.LoadCredentialsFile('google_api_cred.txt')

    #Create local instance of Google Drive
    # drive = GoogleDrive(gauth)

    ##Running
    # gdriveObj = GoogleDriveOps(drive)
    
    #list all files on gdrive
    # all_files = gdriveObj.list_all_gdrive_files('your_folder_id')

    #creating a folder
    # gdriveObj.create_folder_in_gdrive('folder_created_with_python')
  
    # print([(item['id'], item['title']) for item in all_files])