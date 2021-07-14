# Optimal exact solution for dynamic min sum set cover
# Runs in exponential time

from copy import copy

def mtf( permutation, element ):
    for index in range( len( permutation ) ):
        if permutation[ index ] == element:
            return [element] + permutation[ :index ] + permutation[ (index+1): ], index + 1
    return None

def solve( permutation, sets ):
    if sets == []:
        return 0, [ permutation ]
    ans = 1234567890
    curset = sets[ 0 ]
    final_permutations = []
    for elem in curset:
        newpermutation, cost = mtf( permutation, elem )
        rec_cost, rec_permutations = solve( newpermutation, sets[ 1 : ] )
        if rec_cost + cost < ans:
            final_permutations = rec_permutations
            ans = rec_cost + cost
    return ans, [ permutation ] + final_permutations

def mtf_opt( N, requests ):
    return solve( [ i for i in range( N ) ], requests )
