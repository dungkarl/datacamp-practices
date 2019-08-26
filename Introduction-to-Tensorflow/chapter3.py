
import tensorflow as tf 
import numpy as np 
import pandas as pd 

tf.reset_default_graph()
tf.enable_eager_execution()

inputs = tf.constant([[1, 35]])
weights = tf.Variable([[-0.05], [-0.01]])
bias = tf.Variable([0.05])

product = tf.matmul(inputs, weights)
dense = tf.keras.activations.sigmoid(product, bias)

print(dense)
