__author__ = 'otto'
# Libraries Made by me
import data_generator
from code_utils import *
# Libraries that are out there for you to download
import theano
import matplotlib

training_data =  data_generator.generate_n_training_data_points(n = 100)
validation_data = data_generator.generate_n_validation_data_points(n = 100)


time = 0

while True:
    ## Should we kill the algorithm if there is a timeout or if the user asks so?
    if end_algorithm_is_good_idea(time,userControl= False, discrete_timeout_limit= 999) is True:
        print "================= \nAlgorithm a kill\nIteration no." + str(time) + "\n================="
        break
    else:
        time = time + 1

    ########## The algorithm

