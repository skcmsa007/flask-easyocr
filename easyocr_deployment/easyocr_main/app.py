import os
from flask import  request
from flask_api import FlaskAPI
from werkzeug.utils import secure_filename
from flask import jsonify
import cv2
import easyocr
import time
import configparser
#"en", "es", "th", "ch_sim", "fr","ar"


app = FlaskAPI(__name__)
app.name="easyocr_flask"

reader_ar = easyocr.Reader(['ar'])
reader_en = easyocr.Reader(['en'])
reader_fr=easyocr.Reader(['fr'])
reader_es=easyocr.Reader(['es'])
reader_th=easyocr.Reader(['th'])
reader_ch_sim=easyocr.Reader(['ch_sim'])
reader_pt=easyocr.Reader(['pt'])
reader_vi=easyocr.Reader(['vi'])
reader_id=easyocr.Reader(['id'])
# def get_reader(lang):
#     reader = easyocr.Reader([lang,'en'])
#     return reader


@app.route("/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        lang_= request.args.get('lang')
        print(lang_)
        lang=lang_.strip()
        # print("received data is ::",lang,"type is ::", type(lang))
        # print("request received")
        if request.files:
            img=request.files["image"]
            # print("img is::",img)
            img_byte=img.read()
            red="reader_"+lang
            reader=globals()[red]
            res=easyocr_pred(img_byte,reader,lang)
            return res

    return {"status":200}

def easyocr_pred(img,reader,lang):
    if lang in ["ar","th"]:
        result=reader.recognize(img)
    else:
        result = reader.readtext(img)

    # result=reader.readtext_batched(img)
    # print(result)
    #return jsonify(result)
    return str(result)
    
if __name__=="__main__":
    app.run(host="0.0.0.0",port=8989,debug=False)
    # app.run(debug=True)

