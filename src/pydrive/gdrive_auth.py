from pydrive.auth import GoogleAuth

#this will authenticate with local web browser
gauth = GoogleAuth()
gauth.LocalWebserverAuth()

#after auth, save cred to a file to avoid re-auth when run program next time
gauth.SaveCredentialsFile('google_api_cred.txt')