import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            for fileName in files:
                local_path=os.path.join(root,fileName)
                relative_path=os.path.relpath(local_path,file_from)
                dropbox_path=os.path.join(file_to,relative_path)
                with open(local_path,'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))
    
def main():
    access_token = 'ASbm26LgPY4AAAAAAAAAAQz0vMGbf4RSFwN84fbLOn13F_sZMa_PX5u4XlWum7Xb'
    transferData = TransferData(access_token)
    file_from=input("Enter File Path to Tranfer")
    file_to=input("Enter File Path to Upload")
    transferData.upload_file(file_from,file_to)
    print("File has been Moved")

main()