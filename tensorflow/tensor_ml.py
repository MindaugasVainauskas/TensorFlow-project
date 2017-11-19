import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot = True)

x = tf.placeholder(tf.float32, [None, 784])
y_ce = tf.placeholder(tf.float32, [None, 10])

W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x,W) + b)

cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ce * tf.log(y), reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.4).minimize(cross_entropy)


sess = tf.InteractiveSession()

#Set up saver to save model once its ready
save_session = tf.train.Saver()

tf.global_variables_initializer().run()

for _ in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys})

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_ce, 1))

accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# Save session in temp folder with given path
save_model = save_session.save(sess, "/tmp/tensor_model.ckpt")
print(sess.run([accuracy], feed_dict={x: mnist.test.images, y_ce: mnist.test.labels}))
