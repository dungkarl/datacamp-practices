"""
	Introduction to Tensorflow
	API 1.13.1
"""
import tensorflow as tf 
import pandas as pd 
import numpy as np 

# Constant and Variable in tensorflow
tf.enable_eager_execution()
print(tf.__version__)
#tf.reset_default_graph() # Xóa các biến và session đã sử dụng trước đó
# sess = tf.Session()
# init = tf.global_variables_initializer()

# sess.run(init)
# const_a = tf.constant(2, dtype=tf.float32)
# print(sess.run(const_a))
A34 = tf.fill([3, 4], 9)
B34 = tf.ones_like(A34)
C1 = tf.constant([1, 2, 3, 4])
A1 = tf.Variable([1, 2, 3, 4])
print(A1)
# print(sess.run(A34))
# print(sess.run(B34))
# print(sess.run(C1))

# print(type(sess.run(C1)))


print(A34)

# print(sess.run(A1))

#print(C1.numpy())

# Variable

#B1 = A1


#print(sess.run(B1))

"""
	Basic operations
"""

# Define tensors A1 and A23 as constants
A1 = tf.constant([1, 2, 3, 4])
A23 = tf.constant([[1, 2, 3], [1, 6, 4]])
B1 = tf.ones_like(A1)
B23 = tf.ones_like(A23)
C1 = tf.multiply(A1, B1)
C23 =tf.multiply(A23, B23)
print(C1)
print(C23)

# print(sess.run(C1))
# print(sess.run(C23))

# 

X = tf.constant([[1, 2], [2, 1], [5, 8], [6, 10]])
b = tf.constant([[1], [2]])
y = tf.constant([[6], [4], [20], [23]])

ypred = tf.matmul(X, b)

error = tf.subtract(y, ypred)


print(error.numpy())


