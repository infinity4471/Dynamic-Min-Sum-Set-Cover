from distance import dist_seq

def doubly_stochastic( matrix ):
    N = len( matrix )
    for i in range( N ):
        s = 0
        for j in range( N ):
            s += matrix[ i ][ j ]
        if abs( s - 1 ) > 1e-1:
            return False
    for j in range( N ):
        s = 0
        for i in range( N ):
            s += matrix[ i ][ j ]
        if abs( s - 1 ) > 1e-1:
            return False
    return True

def test( total, seq ):
    for matrix in seq:
        if not doubly_stochastic( matrix ):
            print("Error, matrix:", matrix, "is not doubly stochastic!")
            return False
    distance = dist_seq( seq )
    if distance % 2:
        print("double distance is not even?")
        return False
    distance /= 2
    if abs( total - distance ) > 1e-2:
        print("Error!, For sequence of matrices:")
        for matrix in seq:
            print("\n")
            print( matrix )
            print("\n")
        print(f"distance by LP: {total} actual distance is: {dist_seq(seq)}")
        return False
    return True
