import numpy as np
from datetime import datetime
from random import randrange, seed

from linear_programs import lp_paging
from fractional_paging import greedy_paging

seed(datetime.now())

counter = 0
while True:
    N = 1 + randrange( 7 )
    T = 2 + randrange( 6 )
    r = 1 + randrange( 6 )
    requests = []
    for _ in range( T ):
        v = randrange( N )
        requests.append( v )
    print(f"Testcase: N = {N}, T = {T}, r = {r}, requests = ", requests )
    val, x = lp_paging( N, requests, r )
    val = np.round( val, 3 )
    print(f"Objective function optimal value: {val}" )

    verify = 0
    prev = None
    greedy = greedy_paging( N, requests, r )
    print(f"Greedy solution: {greedy}")
    if r * abs( greedy - val ) > 1:
        print("Problem with testcase:\n")
        print("requests = ", requests )
        print("N = ", N )
        print("r = ", r )
        print(f"Found greedy = {greedy} and LP optimal = {val}")
        break
    counter += 1
    print(f"PASSED {counter}")
