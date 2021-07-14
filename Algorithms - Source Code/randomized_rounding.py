import numpy as np

from linear_programs import lp_mtf
from beautify import print_matrices, return_matrices
from stochastic import kendall_tau_distance
from mtf_optimal import mtf
from testing import test

def greedy_randomized( N, requests ): #bad on expectation, O(N) apx
    T = len( requests ) + 1
    val, vector = lp_mtf( N, requests )
    matrix_sequence = return_matrices( vector, T, N )

    test( val, matrix_sequence )

    permutation = np.arange( N )
    total_cost, permutations = 0, [ permutation ]
    for t in range( 1, T ):
        front_element = np.random.choice( np.arange( N ), p = matrix_sequence[ t ][ :, 0 ] )
        permutation, new_cost = mtf( permutation, front_element )
        total_cost += new_cost
        permutations.append( permutation )
    return permutations, total_cost

def randomized_rounding( N, requests ): #skutella based rounding, O(log^2 N) approximation
    T = len( requests ) + 1
    permutation = np.arange( N )
    alpha = [ np.random() for _ in range( N ) ]
    val, vector = lp_mtf( N, requests )
    matrix_sequence = return_matrices( N, requests )
    matrix_sequence = [ mat * np.log( N ) for mat in matrix_sequence ]
    total_cost = 0
    for t in range( 1, T ):
        order = []
        for elem in range( N ):
            s = 0
            for i in range( N ):
                s += matrix_sequence[ t ][ elem ][ i ]
                if s > alpha[ elem ]:
                    order.append( i )
                    break
        ordering = {}
        for i in range( N ):
            if not order[ i ] in ordering.keys():
                ordering[ order[ i ] ] = []
            ordering[ order[ i ] ].append( i )
        new_permutation = []
        for i in range( N ): #ties broken lexicographically
            new_permutation += ordering[ i ]
        total_cost += kendall_tau_distance( new_permutation, permutation )
        permutation = new_permutation
    return total_cost

