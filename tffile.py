import tensorflow as tf
from skimage import io
hello=tf.constant("hello,world")
sess=tf.Session()
print sess.run(hello)
a=tf.constant(10)
b=tf.constant(32)
print sess.run(a+b)

