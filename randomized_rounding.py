import numpy as np

from lp import solve_lp
from beautify import print_matrices, return_matrices
from mtf_optimal import mtf
from testing import test

def greedy_randomized( N, requests ): #bad on expectation, O(N) apx
    T = len( requests ) + 1
    val, vector = solve_lp( N, requests )
    matrix_sequence = return_matrices( vector, T, N )

    test( val, matrix_sequence )

    permutation = [ i for i in range( N ) ]
    total_cost, permutations = 0, [ permutation ]
    for t in range( 1, T ):
        front_element = np.random.choice( np.arange( N ), p = matrix_sequence[ t ][ :, 0 ] )
        permutation, new_cost = mtf( permutation, front_element )
        total_cost += new_cost
        permutations.append( permutation )
    return permutations, total_cost
