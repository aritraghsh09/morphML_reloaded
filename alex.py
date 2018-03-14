#####################################
#alex.py
#
#Applying Alexnet to SDSS Galaxy Images. 
#Based on TFLearn Examples on Github
######################################


from __future__ import division, print_function, absolute_import
import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.normalization import local_response_normalization
from tflearn.layers.estimator import regression
from tflearn.data_utils import image_preloader

# loading data
TrainDataPath = '/path/to/training/data'
TestDataPath = '/path/to/test/data'
modelPath = 'path/to/save/checkpoints' #end with a name which is prefixed to any file model file that is saved by TF Learn

#X is array of images and Y is the corresponding array of labels
X, Y = image_preloader(TrainDataPath, image_shape=(120, 120),mode='folder', categorical_labels=True, normalize=True, files_extension='.jpg')
X_test, Y_test = image_preloader(TestDataPath, image_shape=(120, 120), mode='folder', categorical_labels=True,normalize=True,files_extension='.jpg')
print('Dataset Loaded')

# building AlexNet
network = input_data(shape=[None, 120, 120, 3]) #since we do training in batches, the first None serves as to empower us to choose any batch size that we may want
network = conv_2d(network, 96, 11, strides=4, activation='relu')
network = max_pool_2d(network, 3, strides=2)
network = local_response_normalization(network)
network = conv_2d(network, 256, 5, activation='relu')
network = max_pool_2d(network, 3, strides=2)
network = local_response_normalization(network)
network = conv_2d(network, 384, 3, activation='relu')
network = conv_2d(network, 384, 3, activation='relu')
network = conv_2d(network, 256, 3, activation='relu')
network = max_pool_2d(network, 3, strides=2)
network = local_response_normalization(network)
network = fully_connected(network, 4096, activation='tanh')
network = dropout(network, 0.5)
network = fully_connected(network, 4096, activation='tanh')
network = dropout(network, 0.5)
network = fully_connected(network, 3, activation='softmax')

#training method and parameters 
network = regression(network, optimizer='momentum',loss='categorical_crossentropy',learning_rate=0.001)

# training
model = tflearn.DNN(network, checkpoint_path=modelPath, max_checkpoints=2, tensorboard_verbose=0)

#model.load("/path/to/checkpoint")

model.fit(X, Y, n_epoch=1000, validation_set=(X_test,Y_test), shuffle=True, show_metric=True, batch_size=64, snapshot_step=None, snapshot_epoch=True, run_id='alex')

