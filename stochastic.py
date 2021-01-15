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
