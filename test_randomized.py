from stochastic import generate
import numpy as np
from random import random
from mtf_optimal import mtf
from distance import find_dist

def find_expectations( permutation, matrix, rounds = 50000 ):
    N = len( permutation )
    freq = np.zeros( ( N, N ) )
    total = 0
    for rep in range( rounds ):
        cost = 0
        prev_permutation = permutation
        for elem in permutation:
            if matrix[ elem ][ 0 ] > 0:
                p = random()
                if p <= matrix[ elem ][ 0 ] or permutation[ 0 ] == elem:
                    permutation, cost = mtf( permutation, elem )
                    break
        if cost > 0 :
            total += cost - 1
        for i in range( N ):
            freq[ permutation[ i ] ][ i ] += 1
        permutation = prev_permutation
    freq /= float( rounds )
    total /= float( rounds )
    return np.round( freq, 3 ), total

def test_randomized( N ):
    counter = 0
    permutation = [ i for i in range( N ) ]
    initial = np.identity( N )
    matrix = generate( N )
    print("Testcase with matrix:\n")
    print( matrix )
    freq, total = find_expectations( permutation, matrix )
    if find_dist( matrix, freq ) + total <= find_dist( initial, matrix ):
        counter += 1
        print(f"PASSED {counter}")
    else:
        print("Problem with doubly stochastic matrix:\n")
        print( matrix )
        return False
    return True

#print( find_expectations( [ 0, 1, 2 ], [ [ 0, 1, 0 ], [ 0.75, 0, 0.25 ], [ 0.25, 0, 0.75 ] ] ) )
