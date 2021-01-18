import numpy as np

def try_expectation( N ):
    bins = np.zeros( N )
    total, s = 0, 0
    for i in range( N ):
        index = np.random.randint( N )
        bins[ index ] += 1
    for i in range( N ):
        s += bins[ i ]
        total += abs( s - i - 1 )
    return total

def monte_carlo( N, rounds = 50 ):
    expectation = 0
    for _ in range( rounds ):
        expectation += try_expectation( N )
    expectation /= float( rounds )
    return expectation
