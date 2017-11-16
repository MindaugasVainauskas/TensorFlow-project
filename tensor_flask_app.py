from flask import Flask, render_template, url_for, request
import numpy as np
import base64
from PIL import Image
import re
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

# Processing the drawn image using adaptation of code from:
# https://stackoverflow.com/questions/42762269/python-flask-wtforms-read-image-from-canvas-dataurl-instead-of-form-input-data
@app.route('/', methods=['POST'])
def get_image(): #need to process data url coming from image
    image_string = request.values['imageBase64']
    # Line below cuts of first part of response string to only leave base 64 byte array for further processing
    image_b64 = re.sub('^data:image/png;base64,', '', image_string)
    print(image_b64)
    image_bin = base64.decodebytes(image_b64.encode('utf-8'))
    print('Image url converted to binary:')
    print('========= binary byte array ============')
    print(image_bin)    
    return ''

app.run(host='127.0.0.1', debug=True)
