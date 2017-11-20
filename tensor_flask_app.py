from flask import Flask, render_template, url_for, request
import numpy as np
import base64, io, re
from PIL import Image
import tensorflow as tf

import tensor_ml

app = Flask(__name__)

x = tf.placeholder(tf.float32, shape=[None, 784])

@app.route('/')
def hello_world():
    return render_template('index.html')

# Processing the drawn image using adaptation of code from:
# https://www.reddit.com/r/learnpython/comments/6lqsrp/converting_a_dataurl_to_numpy_array/
@app.route('/', methods=['POST'])
def get_image(): #need to process data url coming from image
    img_size = 28, 28  # Size that will be neded for the application to process image
    image_url = request.values['imageBase64']  # Get the dataUrl from page
    image_string = re.search(r'base64,(.*)', image_url).group(1)  # Get the actual byte string from it
    image_bytes = io.BytesIO(base64.b64decode(image_string))  # Convert it to bytes array
    image = Image.open(image_bytes)  # Make it to PIL image
    image = image.resize(img_size, Image.ANTIALIAS)  # Resize the image to 28x28 size for use with tensorflow
    image_array = np.array(image)[:,:,0]
   # image.show()  # Display image

    # Restore tensorflow session
    sess = tf.Session()
    saver = tf.train.import_meta_graph('tmp/tensor_model.meta')
    saver.restore(sess, 'tmp/tensor_model')

    predicted_number = sess.run(feed_dict={x: image_array})
    print(predicted_number)
    return ''

app.run(host='127.0.0.1', debug=True)
