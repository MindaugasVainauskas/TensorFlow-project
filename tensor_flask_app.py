from flask import Flask, render_template, url_for, request
import numpy as np
import base64, io, re
from PIL import Image
import tensorflow as tf

import tensor_ml as ten

app = Flask(__name__)

guessNum = 0

@app.route('/')
def hello_world():
    return render_template('index.html', guessNum = guessNum)

# Processing the drawn image using adaptation of code from:
# https://www.reddit.com/r/learnpython/comments/6lqsrp/converting_a_dataurl_to_numpy_array/
@app.route('/', methods=['POST', 'GET'])
def get_image(): #need to process data url coming from image
    img_size = 28, 28  # Size that will be neded for the application to process image
    image_url = request.values['imageBase64']  # Get the dataUrl from page
    image_string = re.search(r'base64,(.*)', image_url).group(1)  # Get the actual byte string from it
    image_bytes = io.BytesIO(base64.b64decode(image_string))  # Convert it to bytes array
    image = Image.open(image_bytes)  # Make it to PIL image
    image = image.resize(img_size, Image.ANTIALIAS)  # Resize the image to 28x28 size for use with tensorflow
    image = image.convert('L')
    image_array = np.array(image)
    image_array = image_array.flatten()

    # # Restore tensorflow session
    with tf.Session() as sess:
        saver = tf.train.import_meta_graph('tmp/tensor_model.meta')
        saver.restore(sess, tf.train.latest_checkpoint('tmp/'))

        predict_number = tf.argmax(ten.y, 1)
        predicted_number = ten.sess.run([predict_number], feed_dict={ten.x: [image_array]})
        guessNum = predicted_number[0][0]
        guessNum = int(guessNum)
        print(guessNum)

    return render_template('index.html', guessNum = guessNum)

app.run(host='127.0.0.1', debug=True)
