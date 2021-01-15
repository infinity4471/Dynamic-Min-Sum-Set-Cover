def find_dist( A, B ):
    N = len( A )
    total = 0
    for i in range( N ):
        total_row = 0
        for k in range( N ):
            s1, s2 = 0.0, 0.0
            for j in range( k ):
                s1 += A[ i ][ j ]
                s2 += B[ i ][ j ]
            total_row += abs( s1 - s2 )

        total += total_row
    return total

def dist_seq( A ): #receives a sequence of doubly stochastic matrices
    total = 0
    for i in range( 1, len( A ) ):
        total += find_dist( A[ i ], A[ i - 1 ] )
    return total
