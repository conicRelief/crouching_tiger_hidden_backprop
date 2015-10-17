__author__ = 'otto'
import data_generator
from code_utils import *

import datetime

training_data =  data_generator.generate_n_training_data_points(n = 100)
validation_data = data_generator.generate_n_validation_data_points(n = 100)




def printWeights():
    pass

iteration = 0

while True:

    if end_algorithm_is_good_idea(iteration,userControl= False) is True:
        print "================= \nAlgorithm a kill\nIteration no." + str(iteration) + "\n================="
        break
    else:
        iteration = iteration + 1



