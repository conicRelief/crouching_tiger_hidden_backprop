import itertools

__author__ = 'otto'
import random
import  numpy as np
from matplotlib import pyplot as plt
import pylab


"""
This File generates our data points  It has three methods.
One that generates training data.
One that generates validation data
One that visualizes training data.
"""
def plus_or_minus(term):
    return random.randint(-term,term)

def squidmoid(inpx,stretch_factor_x = 100.00, stretch_factor_y = 200.00, random_interval_range = 200, yoffset = 500):
    return  float(stretch_factor_y/(1 + np.exp(-((inpx-500)/stretch_factor_x)**2))) + plus_or_minus(random_interval_range) + yoffset

def generate_n_training_data_points(y_off, n = 100,):
    stx = random.randint(200,300) # xStretch
    sty = random.randint(400,600) # yStretch
    xs =  [random.randint(0,1000) for x in range(n)]
    ys =  [float(squidmoid(z,yoffset = y_off,stretch_factor_y = float(sty),stretch_factor_x= float(stx))) for z in xs]
    return zip(xs, ys)

def generate_n_validation_data_points(n = 100):
    """
    Todo. Generate n training data points and call it set V. Such that V union T is the null set.
    Returned values will assume the form:
    [(Class1,[x1,y1]),(Class2,[x2,y2]),...,(Classn,[xn,yn])]
    """
    return []
def static_var(varname, value):
    def decorate(func):
        setattr(func, varname, value)
        return func
    return decorate

@static_var("counter", 0)
def visualize_data(data = None):
    """
    Todo. Takes a list of lists. Then maps all of those lists on a 2d plot.
    Each list contains two different colorings of data.
    A list of list contains len(list_of_list) * 2 different colorings.
    Visualization will be usefull in showing step by step by step evolution of isomomorphic transformation.
    """
    colors = itertools.cycle(["r", "b", "g"])

    visualize_data.counter += 1
    for dt in data:
        x,y = zip(*dt)
        plt.scatter(x,y,color = colors.next())
    plt.show()


    pass

