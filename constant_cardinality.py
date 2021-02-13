#Constant Cardinality Sets Algorithms
#O(r^2) approximation where the request sequence R_t has cardinality at most r

import numpy as np

from linear_programs import solve_lp
from beautify import print_matrices, return_matrices
from mtf_optimal import mtf
from testing import test

def get_heaviest( matrix ):
    N = len( matrix )
    argmax = 0
    for element in range( N ):
        if matrix[ element ][ 0 ] > matrix[ argmax ][ 0 ]:
            argmax = element
    return argmax

def heaviest_to_front( N, requests ):
    T = len( requests ) + 1
    val, solutions = solve_lp( N, requests )
    solutions = np.round( solutions, 3 )
    seq = return_matrices( solutions, T, N )

    test( val, seq ) #check if LP matrix sequence makes sense

    permutation = [ i for i in range( N ) ]
    total_cost, permutations = 0, [ permutation ]
    for t in range( 1, T ):
        front_element = get_heaviest( seq[ t ] )
        permutation, new_cost = mtf( permutation, front_element )
        total_cost += new_cost
        permutations.append( permutation )
    return permutations, total_cost
