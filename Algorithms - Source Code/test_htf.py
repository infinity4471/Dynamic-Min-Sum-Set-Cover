#Test generator for heaviest to front algorithm
#Null hypothesis: Let OPT be the fractional solution returned by LP
#and let HTF be the solution by the greedy heaviest to front algorithm
#then HTF \leq 2r^2 OPT where r is the cardinality of the service sets

import numpy as np
from datetime import datetime
from random import randrange, seed

from lp import lp_mtf
from constant_cardinality import heaviest_to_front
from testing import test
from beautify import return_matrices

seed(datetime.now())

counter = 0
while True:
    N = 1 + randrange( 5 )
    T = 2 + randrange( 4 )
    r = 1 + randrange( 3 )
    requests = []
    for _ in range( T - 1 ):
        request = []
        for i in range( r ):
            v = randrange( N )
            request.append( v )
        requests.append( request )
    print(f"Testcase: N = {N}, T = {T}, r = {r}, requests = ", requests )
    val, x = lp_mtf( N, requests )
    val = np.round( val, 3 )
    print(f"Objective function optimal value: {val}" )
    seq = return_matrices( x, T, N )
    if not test( val, seq ):
        print("FAIL ON TEST!")
        break

    verify = 0
    prev = None
    _, greedy = heaviest_to_front( N, requests )
    print(f"Greedy solution: {greedy}")
    if greedy > 2*r*val + T or greedy < val:
        print("\nProblem with testcase:")
        print("requests = ", requests )
        print("N = ", N )
        print("r = ", r )
        print(f"Found greedy = {greedy} and LP optimal = {val}")
        break
    counter += 1
    print(f"PASSED {counter}")
