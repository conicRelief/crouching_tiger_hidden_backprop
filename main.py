__author__ = 'otto'
# Libraries Made by me

import data_generator
from code_utils import *
import theano_helper

# Libraries that are out there for you to download
import theano
import numpy as np

training_data_class_a =  data_generator.generate_n_training_data_points(0,  n = 1000)
training_data_class_b =  data_generator.generate_n_training_data_points(360,n = 1000)

data_generator.visualize_data([training_data_class_a, training_data_class_b])

time = 0

# dances_with_theano.call_me(training_data_class_a,[[0,0],[0,0]],[0,1])
#error function = meanSquared error.
# l(theta, D) =  (1/|D|)#sum( yi - y_double_dot(di))


layer_1_parameters = [[0,0],[0,0]]
layer_2_parameters = [0,0]
# print ">>>>",dances_with_theano.evaluate(training_data_class_a[0],layer_1_parameters,layer_2_parameters)

# [[0 , data] for data in training_data_class_b]



while True:
    ## Should we kill the algorithm if there is a timeout or if the user asks us to?
    if end_algorithm_is_good_idea(time,userControl= False, discrete_timeout_limit= 999) is True:
        print "================= \nAlgorithm a kill\nIteration no." + str(time) + "\n================="
        break
    else:
        time = time + 1
    ########## The algorithm
    error = np.abs( sum([ 1 - theano_helper.evaluate(data,layer_1_parameters,layer_2_parameters) for data in training_data_class_a]))
    error = error + np.abs( sum([ 0 - theano_helper.evaluate(data,layer_1_parameters,layer_2_parameters) for data in training_data_class_b]))
    print error
    # layer_1_parameters = layer_1_parameters - gamma*derror/dlayer_1_parameters
    # layer_2_parameters = layer_2_parameters - gamma*derror/dlayer_2_parameters



