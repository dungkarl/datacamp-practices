"""
	Imput data
	processing data by tensorflow
"""

import tensorflow as tf 
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 

tf.enable_eager_execution()
tf.reset_default_graph()
data_path = 'kc_house_data.csv'
housing = pd.read_csv(data_path)
print(housing.head())


# Use a numpy array to define price as a 32-bit float
price = np.array(housing['price'], np.float32)
waterfront = tf.cast(housing['waterfront'], tf.bool)

size = np.array(housing['sqft_living'], np.float32)


intercept = tf.Variable(0.1, np.float32)
slope = tf.Variable(0.1, np.float32)


def linear_regression(intercept, slope, features=size):
	"""

	"""
	return intercept + slope*features


def loss_function(intercept, slope, targets=price, features=size):

	predictions = linear_regression(intercept, slope)
	return tf.keras.losses.mse(targets, predictions)

#opt = tf.keras.optimizers.Adam()
#opt = tf.contrib.keras.optimizers.Adam()
opt = tf.train.AdamOptimizer()

for i in range(1000):
	opt.minimize(lambda:loss_function(intercept, slope), var_list=[intercept, slope])
	if i%10==0:
		print(loss_function(intercept, slope))




# Print price and waterfront
# print(price)
# print(waterfront)

# plt.scatter( housing['sqft_living'], housing['price'])
# plt.title('House Price per Size')
# plt.xlabel('Size')
# plt.ylabel('Price')
# plt.show()


