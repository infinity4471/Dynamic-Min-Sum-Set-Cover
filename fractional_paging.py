import copy
import numpy as np
from distance import find_dist

def find_last( mat, requests, index, r ):
    N = len( mat )
    INF = 198248912894
    pos = [ False ] * N
    big = [ False ] * N
    first_time = [ INF ] * N
    for e in range( N ):
        if mat[ e ][ index ] > 0:
            pos[ e ] = True
        cumulative = 0
        for i in range( index + 1 ):
            cumulative += mat[ e ][ i ]
        if r * cumulative >= 2:
            big[ e ] = True
        for i in range( len( requests ) ):
            if e == requests[ i ]:
                first_time[ e ] = i
                break
    myelem = -1
    for e in range( N ):
        if e == requests[ 0 ]:
            continue
        if pos[ e ] and big[ e ]:
            return e
    for e in range( N ):
        if not pos[ e ]:
            continue
        if myelem == -1 or first_time[ e ] > first_time[ myelem ]:
            myelem = e
    return myelem

def find_next( N, requests, r, mat ):
    element = requests[ 0 ]
    pos = -1
    for i in range( N ):
        if r * mat[ element ][ i ] >= 1:
            pos = i
            break
    res = copy.copy( mat )
    if pos == 0:
        return res
    res[ element ][ 0 ] = 1.0/r
    res[ element ][ pos ] -= 1.0/r
    for i in range( pos ):
        move_index = find_last( res, requests, i, r )
        res[ move_index ][ i ] -= 1.0/r
        res[ move_index ][ i + 1 ] += 1.0/r
    return res

def greedy_paging( N, requests, r ):
    T = len( requests ) + 1
    lst = [ np.identity( N ) for _ in range( T ) ]
    T = len( requests ) + 1
    total = 0
    for t in range( 1, T ):
        lst[ t ] = find_next( N, requests, r, lst[ t - 1 ] )
        total += find_dist( lst[ t ], lst[ t - 1 ] )
        requests.pop( 0 )

    return total

