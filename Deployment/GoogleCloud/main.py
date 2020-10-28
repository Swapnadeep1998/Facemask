from flask import Flask, render_template, jsonify, request
import os
from flask_cors import CORS, cross_origin
from facemask_utils.utils import Decode_Image_Base64
from predict import FaceMask


os.putenv('LANG','en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

application=Flask(__name__)
CORS(application)


class ClientApp:
    def __init__(self):
        self.fileName='imgFile.jpg'
        self.classifier=FaceMask(self.fileName)

@application.route("/",methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@application.route("/predict",methods=['POST'])
@cross_origin()
def predict():
    data=request.get_json('data')   
    imgString=data['data']  
    
    dcodeBas64=Decode_Image_Base64(imgString,clApp.fileName)
    dcodeBas64.decode()
    result=clApp.classifier.classify()   
    return jsonify(result)



clApp=ClientApp()  

if __name__=="__main__":    
    application.run(debug=False)