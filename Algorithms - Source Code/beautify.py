import numpy as np
from distance import dist_seq

def print_matrices( x, T, N ):
    matrices = []
    for t in range( T ):
        A = []
        for e in range( N ):
            A.append( [] )
            for i in range( N ):
                A[ e ].append( x[ t * N * N + e * N + i ] )
            prev = np.round( A, 3 )
        matrices.append( A )
        print(f"matrix for time {t}: \n\n", np.round( A, 3 ) )
    dist = np.round( dist_seq( matrices ) )
    print(f"Actual distance {dist}")
    print("\n")

def return_matrices( x, T, N ):
    seq = []
    for t in range( T ):
        A = []
        for e in range( N ):
            A.append( [] )
            for i in range( N ):
                A[ e ].append( x[ t * N * N + e * N + i ] )
        seq.append( np.round( A, 3 ) )
    return seq
