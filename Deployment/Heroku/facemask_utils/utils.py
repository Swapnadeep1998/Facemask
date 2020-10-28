import base64

class Decode_Image_Base64:
    def __init__(self,imgString,fileName):
        self.imgString=imgString
        self.fileName=fileName
    def decode(self):
        imgString=self.imgString        
        fname=self.fileName
        imgData=base64.b64decode(imgString)
        with open(fname,'wb') as f:
            f.write(imgData)
            f.close()

class Encode_Image_Base64:
    def __init__(self,imgPath):
        self.file_path=imgPath
    def encode(self):
        imgPath=self.file_path
        with open(imgPath,'rb') as f:
            return base64.b64encode(f.read())


