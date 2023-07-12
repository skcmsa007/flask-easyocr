import os
from flask import Flask, flash, request, redirect, url_for
from flask_api import FlaskAPI
#from werkzeug.utils import secure_filename
from flask import jsonify
import cv2
import easyocr
#from utils import *
reader = easyocr.Reader(['th','en'])

UPLOAD_FOLDER = './img_dir'

app = FlaskAPI(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print("request received")
        if request.files:
            img=request.files["image"]
            img_byte=img.read()
            print(img)
            ip_path=os.path.join(UPLOAD_FOLDER,img.filename)
            img.save(os.path.join(UPLOAD_FOLDER,img.filename))
            print(ip_path)
            res=easyocr_pred(img_byte)
            print(type(res))
            return res
    return {"status":200}

def image_shape(image1):
    img = cv2.imread(image1)
    img_dimensions = img.shape
    d={"shape":img_dimensions}
    return d

def easyocr_pred(img):
    global reader
    result = reader.readtext(img)
    print(result)
    #return jsonify(result)
    return str(result)
    
if __name__=="__main__":
    app.run(host="0.0.0.0",port=8989,debug=False,threaded=True)
