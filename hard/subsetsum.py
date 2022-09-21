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
        if round(.999*t) <= s and round(1.001*t) >= s:
        #if s == t:
            print(indexset, s, t, end = ' ')
            print('bingo' if s==t else '')

def trim(L, ratio):
    last = L[0]
    Lnew = [last]
    for j in range(1, len(L)):
        if L[j] > last * ratio:
            Lnew.append(L[j])
            last = L[j]
    return Lnew

def ss2(S, t): # iterative merging, prep for fptas
    L, Lset = [0], {0}
    for p in S:
        M = []
        for x in L:
            if x+p == t:
                #print(L)
                print('yes')
                return
            if x+p < t and x+p not in Lset:
                M.append(x+p)
                Lset.add(x+p)
        L += M
    print('no')

def fptas(S, t, eps): # fptas for subset sum
    n = len(S)
    r = 1.0 + eps/(2.0 * n)
    L, Lset = [0], {0}
    for p in S:
        M = []
        for x in L:
            if x+p == t: 
                #print(L)
                print('yes')
                return
            if x+p < t and x+p not in Lset:
                M.append(x+p)
                Lset.add(x+p)
        L += M
        L.sort()
        L = trim(L, r)
    print('target', t, ' approx. ratio 1.0+', eps, ' approx. sum', L[len(L)-1], ' final list length', len(L), ' not exact')
    print('')

n = 12
max_val = round(.95 * 2**n)
S = gensubset(n, max_val)
#S = [1, 23, 38, 43, 46, 58]
t = round(.5 * sum(S))
print('set ', S, ' target ', t)
subsetsum(S, t)
print('')
ss2(S,t)
print('')

for j in [.4, .2, .1, .05, .01]:
  fptas(S, t, j)

#set  [128941, 177712, 226421, 317169, 435389, 466313, 522297, 523615, 596412, 605529, 626802, 630249, 640644, 670557, 729843, 786586, 816311, 976756, 977042, 992235]  target  5923412
#(4, 6, 7, 8, 9, 11, 12, 18, 19) 5923412 5923412 bingo
