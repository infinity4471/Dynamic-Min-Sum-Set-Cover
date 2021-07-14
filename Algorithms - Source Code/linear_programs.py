import numpy as np
from scipy.optimize import linprog
from distance import dist_seq
from copy import copy

def lp_paging( N, requests, r, method = "simplex" ):
    T = len( requests ) + 1
    coeff = np.zeros( 3 * T * N * N ) # T NxN matrices as well as S^{+}, S^{-}

    def index_splus( time, element, index ):
        return T * N * N + time * N * N + element * N + index
    def index_sminus( time, element, index ):
        return 2 * T * N * N + time * N * N + element * N + index
    def index_elem( time, element, i ):
        return time * N * N + element * N + i

    #construct the  objective function coefficients
    for time in range( T ):
        for element in range( N ):
            for index in range( N ):
                coeff[ index_splus( time, element, index ) ] = 1
                coeff[ index_sminus( time, element, index ) ] = 1

    A = []
    b = []
    for i in range( N ):
        constraint = np.zeros( 3 * T * N * N )
        constraint[ index_elem( 0, i, i ) ] = 1
        A.append( constraint )
        b.append( 1 )

    for t in range( T ): #column sums 1
        for index in range( N ):
            constraint = np.zeros( 3 * T * N * N  )
            for element in range( N ):
                constraint[ index_elem( t, element, index ) ] = 1
            A.append( constraint )
            b.append( 1 )

    for t in range( T ): #row sums to 1
        for element in range( N ):
            constraint = np.zeros( 3 * T * N * N )
            for index in range( N ):
                constraint[ index_elem( t, element, index ) ] = 1
            A.append( constraint )
            b.append( 1 )

    for t in range( 1, T ):
        for element in range( N ):
            for index in range( N ):
                constraint = np.zeros( 3 * T * N * N )
                constraint[ index_splus( t, element, index ) ] = 1
                constraint[ index_sminus( t, element, index ) ] = -1
                for i in range( index + 1 ):
                    constraint[ index_elem( t, element, i ) ] = 1
                    constraint[ index_elem( t - 1, element, i ) ] = -1
                A.append( constraint )
                b.append( 0 )
    A2 = []
    b2 = []

    for t in range( 1, T ):
        constraint = np.zeros( 3 * T * N * N )
        constraint[ index_elem( t, requests[ t - 1 ], 0 ) ] = -1
        A2.append( constraint )
        b2.append( -1.0/float( r ) )
    res = linprog( coeff, A_ub = A2, b_ub = b2, A_eq = A, b_eq = b, method=method )
    return res.fun, res.x


def lp_mtf( N, requests, method = "simplex" ):
    T = len( requests ) + 1
    coeff = np.zeros( 3 * T * N * N ) # T NxN matrices as well as S^{+}, S^{-}

    def index_splus( time, element, index ):
        return T * N * N + time * N * N + element * N + index
    def index_sminus( time, element, index ):
        return 2 * T * N * N + time * N * N + element * N + index
    def index_elem( time, element, i ):
        return time * N * N + element * N + i

    #construct the  objective function coefficients
    for time in range( T ):
        for element in range( N ):
            for index in range( N ):
                coeff[ index_splus( time, element, index ) ] = 0.5
                coeff[ index_sminus( time, element, index ) ] = 0.5

    A = copy( [] )
    b = copy( [] )
    for i in range( N ):
        constraint = np.zeros( 3 * T * N * N )
        constraint[ index_elem( 0, i, i ) ] = 1
        A.append( constraint )
        b.append( 1 )

    for t in range( T ): #column sums 1
        for index in range( N ):
            constraint = np.zeros( 3 * T * N * N  )
            for element in range( N ):
                constraint[ index_elem( t, element, index ) ] = 1
            A.append( constraint )
            b.append( 1 )

    for t in range( T ): #row sums to 1
        for element in range( N ):
            constraint = np.zeros( 3 * T * N * N )
            for index in range( N ):
                constraint[ index_elem( t, element, index ) ] = 1
            A.append( constraint )
            b.append( 1 )

    for t in range( 1, T ):
        for element in range( N ):
            for index in range( N ):
                constraint = np.zeros( 3 * T * N * N )
                constraint[ index_splus( t, element, index ) ] = 1
                constraint[ index_sminus( t, element, index ) ] = -1
                for i in range( index + 1 ):
                    constraint[ index_elem( t, element, i ) ] = 1
                    constraint[ index_elem( t - 1, element, i ) ] = -1
                A.append( constraint )
                b.append( 0 )
    for t in range( 1, T ):
        constraint_set = np.zeros( 3 * T * N * N )
        for elem in requests[ t - 1 ]:
            constraint_set[ index_elem( t, elem, 0 ) ] = 1
        A.append( constraint_set )
        b.append( 1 )
    res = linprog( coeff, A_eq = A, b_eq = b, method="simplex" )
    return res.fun, res.x

