from flask import Flask, render_template, url_for, request
import numpy as np
import base64, io, re
from PIL import Image
import tensorflow as tf

import tensor_ml

app = Flask(__name__)


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
    image = image.convert('L')
    image_array = np.array(image)
    image_array = image_array.reshape(784)
    image_tensor = tf.convert_to_tensor(image_array, np.float32)

    
    x = tf.placeholder(tf.float32, shape=[None, 784])
    y_ = tf.placeholder(tf.float32, shape=[None, 10])
    W = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))

    # Implement regression model
    y = tf.matmul(x,W)+b
    # Restore tensorflow session
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    saver = tf.train.import_meta_graph('tmp/tensor_model.meta')
    saver.restore(sess, tf.train.latest_checkpoint('tmp/'))

    # Evaluate the model accuracy
    correct_pred = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))

    accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
    predict_number = tf.argmax(y, 1)
    predicted_number = predict_number.eval(feed_dict={x: [image_tensor]}, session=sess)
    print(predicted_number)
    return ''

app.run(host='127.0.0.1', debug=True)
