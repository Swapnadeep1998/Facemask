from flask import Flask, render_template, jsonify, request
import os
from flask_cors import CORS, cross_origin
from facemask_utils.utils import Decode_Image_Base64
from predict import FaceMask


os.putenv('LANG','en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app=Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.fileName='imgFile.jpg'
        self.classifier=FaceMask(self.fileName)

@app.route("/",methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/predict",methods=['POST'])
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
    app.run(debug=False)