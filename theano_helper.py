__author__ = 'otto'
import theano.tensor as T
from theano import *
import numpy as np

# This is where I play with theano until I get it right.

w1 =  T.dmatrix("w1")
w2 =  T.dvector("w2")
s_layer = T.dvector("s_layer")
objective = T.tanh(T.dot(w2,T.tanh(T.dot(w1,s_layer) + 1)))
f1 = function([w2,w1,s_layer], objective)


def evaluate(input_layer, layer_1_parameters, layer_2_parameters):
    # w1 is a 2x1 matrix
    # w2 is a 2x2 weight matrix.
    # Realistically its going to look like this.
    #y_double_dot = tanh(dot(tanh(dot(zinput,W2), W1)
    return f1(numpy.array(layer_2_parameters),numpy.array(layer_1_parameters),numpy.array(input_layer))

def input_to_numpy(data):
    return [np.array(x) for x in data]