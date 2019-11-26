"""
simple subset-sum algorithms   RBH 2019

hardest instances have  density 1, where
density is n / log_2( max element in S )
"""

from operator  import mul
from random    import randint
from itertools import chain, combinations
import numpy as np
from copy import deepcopy

def gensubset(n, max_val):
    S = []
    while len(S) < n:
        new = randint(1, max_val)
        if new not in S:
            S.append(new)
    return sorted(S)

def powerset(iterable):
#https://docs.python.org/2/library/itertools.html#recipes
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def subsetsum(S, t): #brute force subset sum
    indices = range(len(S)) # [0 1 .. n-1]
    for indexset in powerset(indices):
        s = sum(S[t] for t in indexset)
        if round(.99*t) <= s and round(1.01*t) >= s:
            print(indexset, s, t, end = ' ')
            print('bingo' if s==t else '')

def ss2(S, t): # iterative merging
    L, Lset = [0], {0}
    for p in S:
        M = []
        for x in L:
            if x+p == t: 
                print(L, 'yes')
                return
            if x+p < t and x+p not in Lset:
                M.append(x+p)
                Lset.add(x+p)
        L += M
    print('no')

n = 6
max_val = round(.95 * 2**n)
S = gensubset(n, max_val)
#S = [1, 23, 38, 43, 46, 58]
t = round(.5 * sum(S))
print('set ', S, ' target ', t)
subsetsum(S, t)
print('')
ss2(S,t)
