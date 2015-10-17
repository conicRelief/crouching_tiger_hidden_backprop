__author__ = 'otto'
import data_generator
import code_utils

import datetime

training_data =  data_generator.generate_n_training_data_points(n = 100)
validation_data = data_generator.generate_n_validation_data_points(n = 100)




def printWeights():
    pass
def end_algorithm_is_good_idea(userControl = False, time_out= 5000):
    # This basically tells us wether or not we want to interrupt the process step by step to see what is going on each layer
    # The interrupt stalls the main loop and asks the user for
    if userControl is True:
        line_read = raw_input( "Press <ENTER> to perform and display next iteration. Type \"exit\" to exit this loop and display weights:  ")
        lev_d = code_utils.levenshtein_distance(line_read.strip().lower(),"exit" )
        if lev_d  <=2:
            printWeights()
            return True
        else:
            return False
    else:
        """
        Todo: Implement Timeout Mechanism. for now we just
        """
        return True

while True:
    if end_algorithm_is_good_idea(userControl= True) is True:
        break

