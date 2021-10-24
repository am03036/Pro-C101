import os
import dropbox
from dropbox.files import WriteMode
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def uploadFile(self,fileFrom,fileTo):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs,files in os.walk(fileFrom):
            for fileName in files:
                localPath = os.path.join(root,fileName)
                relativePath = os.path.relpath(localPath,fileFrom)
                dropboxPath = os.path.join(fileTo,relativePath)
                with open(localPath,'rb') as f:
                    dbx.files_upload(f.read(),dropboxPath,mode=WriteMode('overwrite'))


def main():
    access_token = 'FqVKjz9vRb8AAAAAAAAAAYkNFNNZFcbYJhAS8wuiLQzOWA2cQAaSftWxeLN1_cC7'
    transferData = TransferData(access_token)
    fileFrom = input('Enter the path of the file to be moved: ')
    fileTo = input('Enter the destination: ')
    transferData.uploadFile(fileFrom,fileTo)
    print('File has been moved!')

main()