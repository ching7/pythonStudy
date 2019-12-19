# tf is a computing lib
import tensorflow as tf

# int
print(tf.constant(1))
# float
print(tf.constant(1.))
# double
print(tf.constant(1.,dtype=tf.double))

# boolean
print(tf.constant([True,False]))
# String
print(tf.constant('hello world.'))

# chose tensor device
with tf.device("cpu"):
    print(tf.constant(1).device)