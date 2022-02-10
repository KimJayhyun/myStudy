import tensorflow as tf
import matplotlib.pyplot as plt

initializer1 = tf.random_normal_initializer(mean=0.0, stddev=0.05, seed=0)
initializer2 = tf.random_normal_initializer(mean=0.2, stddev=0.05, seed=1)

a = tf.Variable(initializer1(shape=[10, 100], dtype=tf.float32))
b = tf.Variable(initializer2(shape=[10, 100], dtype=tf.float32))

# print(a.numpy())
# print(b.numpy())

plt.hist(a.numpy().flatten())
plt.hist(b.numpy().flatten())
plt.show()