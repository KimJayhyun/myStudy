import tensorflow as tf


@tf.function
def add(x, y):
    return x + y

# hello  = tf.constant("hi")

# print(hello)

# a = tf.constant(1)
# b = tf.constant(20)

# ## tensorflow v1 방식
# # c = tf.add(a, b)
# # sess = tf.Session()
# # sess.run(c)

# c = add(a, b)

# print(c)    

# tf.matmul()

a = tf.constant(100)
b = tf.constant(120)
c = tf.constant(140)

v = tf.Variable(0)

# 데이터 플로우 그래프 정의하기
