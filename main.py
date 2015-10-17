__author__ = 'otto'
import data_generator
from code_utils import *

import datetime

training_data =  data_generator.generate_n_training_data_points(n = 100)
validation_data = data_generator.generate_n_validation_data_points(n = 100)




def printWeights():
    pass


while True:
    if end_algorithm_is_good_idea(userControl= True) is True:
        print "================= \nAlgorithm a kill \n================="
        break


