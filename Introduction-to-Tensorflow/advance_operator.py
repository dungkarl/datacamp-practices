"""

"""
import tensorflow as tf 
import numpy as np 
import pandas as pd 



tf.enable_eager_execution()
print(tf.__version__)

image = tf.ones([16, 16])
#print(image)

image_vector = tf.reshape(image, (16*16, 1)) # chuyen ve vector 1 chieu co do dai 16*16
image_tensor = tf.reshape(image, (4, 4, 4, 4)) 

# Add three color channels
image_3D = tf.ones([16, 16, 3])

image_vector_3D = tf.reshape(image_3D, (16*16*3, 1))
image_tensor_3D = tf.reshape(image_3D, (4, 4, 4, 4, 3))



def compute_gradient(x_input):
	x = tf.Variable(x_input)
	with tf.GradientTape() as tape:
		tape.watch(x)
		y = tf.multiply(x, x)

	return tape.gradient(y, x).numpy() # 

print(compute_gradient(-1.0))
print(compute_gradient(1.0))
print(compute_gradient(0.0))


# create variable has shape(1,3)

x = tf.fill([1, 3], 3)
x_reshape = tf.reshape(x, (3, 1))
print(x)
print(x_reshape)


output = tf.matmul(x, x_reshape)

predict = tf.reduce_sum(output)
print(predict.numpy())