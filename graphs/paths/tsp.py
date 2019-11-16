"""
brute force tsp    RBH 2019
"""

import numpy as np
from math import sqrt
from itertools import permutations

def euclid_dist(triples): # assuming triples (label, x-coordinate, y-coordinate)
    n = len(triples)
    d = np.full((n,n), 0, dtype = np.uint16)
    for j in range(n):
        for k in range(n):
            z = [0,0]
            for t in range(2):
                z[t] = triples[j][t+1] - triples[k][t+1]
                z[t] *= z[t]
            d[j][k] = round(sqrt(sum(z)))
    return d

def display(points, dist):  # points as above, dist is 2-d array of point-point distances
    n = len(points)
    assert n == len(dist)
    out = ' '
    for j in range(n):
        out += '   ' + points[j][0]
    print(out)
    for j in range(n-1):
        out = points[j][0]
        for k in range(n):
            if j < k: out += ' ' + '{:3}'.format(dist[j][k])
            else: out += '   '
        print(out)

points = (('A', 0, 15), ('B', 5, 60), ('C', 15, 5), ('D', 15, 45), ('E', 30, 30),
    ('F', 50, 25), ('G', 50, 60), ('H', 60, 0), ('I', 85, 5), ('J', 75, 35))

d = euclid_dist(points)
display(points, d)

def tsp(points, dist): # points, dist as in distplay()
    n = len(points)
    assert(n == len(dist))
    indices = [j for j in range(1,n)]
    print(indices)
    cost = 1+n*max([d[j][k] for j in range(n) for k in range(n)]) #upper bound
    for perm in permutations(indices):
        s = d[0][perm[0]] + d[0][perm[n-2]]
        for j in range(1,n-1):
            s += d[perm[j-1]][perm[j]]
        if s < cost: 
            print(s, perm)
            cost = s
     
tsp(points, d)
