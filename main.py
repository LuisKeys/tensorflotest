# Solution is available in the other "solution.py" tab
import tensorflow as tf

# TODO: Convert the following to TensorFlow:
x = tf.constant(10)
y = tf.constant(2)
div = tf.divide(x, y)
z = tf.subtract(tf.cast(div, tf.int32), tf.constant(1))

# TODO: Print z from a session
session = tf.Session()
output = session.run(z)
print(output)    