#tensorflow tutorial for deep mnist

# Download and read mnist data from tensorflow libraries
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)


#save path for the saved session
savePath = 'tmp/tensor_model'

# Import tensorflow and start the session
import tensorflow as tf
sess = tf.InteractiveSession()

# Set placeholders for nodes
x = tf.placeholder(tf.float32, shape=[None, 784])
y_ = tf.placeholder(tf.float32, shape=[None, 10])

# Define Weight and bias
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))


# Initialize the variables so they can be used within session
sess.run(tf.global_variables_initializer())

# Save the session for later use
saver = tf.train.Saver()

# IMplement regression model
y = tf.nn.softmax(tf.matmul(x,W)+b)

# Set cost of prediction
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))


# Set training step size
train_step = tf.train.GradientDescentOptimizer(0.35).minimize(cross_entropy)

# Train the model
for _ in range(3000):
	batch = mnist.train.next_batch(100)
	train_step.run(feed_dict={x: batch[0], y_: batch[1]})
	
# Evaluate the model accuracy
correct_pred = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))

accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

# Print out the accuracy
acc_eval = accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels})
print("Current accuracy: %.2f%%"% (acc_eval*100))	

# Save the path to the trained model
saver.save(sess, savePath)
print('Session saved in path '+savePath)