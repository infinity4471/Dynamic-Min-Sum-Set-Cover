from testing import test
from random import random, seed
from datetime import datetime

import numpy as np

def generate( N, rounds = 1000 ): # generates a NxN doubly stochastic matrix
    seed(datetime.now())
    matrix = np.random.rand( N, N )
    for rep in range( rounds ):
        matrix /= matrix.sum( axis = 1 )[ :, None ]
        matrix /= matrix.sum( axis = 0 )[ None, : ]
    matrix = np.round( matrix, 3 )
    test( 0, [ matrix ] )
    return matrix

def kendall_tau_distance(order_a, order_b):
    pairs = itertools.combinations(range(1, len(order_a)+1), 2)
    distance = 0
    for x, y in pairs:
        a = order_a.index(x) - order_a.index(y)
        b = order_b.index(x) - order_b.index(y)
        if a * b < 0:
            distance += 1
    return distance
