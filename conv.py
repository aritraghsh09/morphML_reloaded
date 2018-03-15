""" Convolutional Neural Network to galaxies
References:
    Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner. "Gradient-based
    learning applied to document recognition." Proceedings of the IEEE,
    86(11):2278-2324, November 1998.
"""

from __future__ import division, print_function, absolute_import

import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.normalization import local_response_normalization
from tflearn.layers.estimator import regression

dataPath = '/gpfs/loomis/project/fas/urry/zw297/dataWithoutTest'
testPath = '/gpfs/loomis/project/fas/urry/zw297/dataTest'
modelPath = '/gpfs/loomis/project/fas/urry/zw297/test_runs/conv/check'

#X is array of images and Y is the corresponding array of labels 
X, Y = image_preloader(dataPath, image_shape=(120, 120), mode='folder', categorical_labels=True, normalize=True, files_extension='.jpg')
testX, testY = image_preloader(testPath, image_shape=(120, 120), mode='folder', categorical_labels=True, normalize=True, files_extension='.jpg')
print('Dataset Loaded')

# Building convolutional network
network = input_data(shape=[None, 120, 120, 3], name='input')
network = conv_2d(network, 32, 3, activation='relu', regularizer="L2")
network = max_pool_2d(network, 2)
network = local_response_normalization(network)
network = conv_2d(network, 64, 3, activation='relu', regularizer="L2")
network = max_pool_2d(network, 2)
network = local_response_normalization(network)
network = fully_connected(network, 128, activation='tanh')
network = dropout(network, 0.8)
network = fully_connected(network, 256, activation='tanh')
network = dropout(network, 0.8)
network = fully_connected(network, 3, activation='softmax')
network = regression(network, optimizer='adam', learning_rate=0.001,
                     loss='categorical_crossentropy', name='target')

# Training
model = tflearn.DNN(network, tensorboard_verbose=0)

model.fit({'input': X}, {'target': Y}, n_epoch=100,
           validation_set=({'input': testX}, {'target': testY}),
           snapshot_step=100, show_metric=True, run_id='conv1')

