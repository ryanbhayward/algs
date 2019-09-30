# simple optimal binary search tree
# simple means each gap probabilty is 0.0
# RBH 2019

import numpy as np
from copy import deepcopy

def special(P): # set entries to (2**j / d)
  p = 1.0
  for j in range(len(P)):
    P[j] = p
    p = 2 * p

def set_probs(P): # scale entries so sum is 1.0
  s = np.sum(P)
  for j in range(len(P)):
    assert(P[j]) > 0
    P[j] = P[j] / s
  
P = np.array([.3, .2, .05, .4, .05])
#P = np.array([.5, .4, .3, .2, .1])
#P = np.array([.1, .2, .3, .4, .5])
#special(P)

set_probs(P)
n = len(P)
W = np.empty(shape=(n,n))
C = np.empty(shape=(n,n),dtype=int)

infinity = n*n*1.0

for j in range(n):
  for k in range(n):
    W[j,k] = 0.0
    C[j,k] = 0

for j in range(n):
  W[j,j] = P[j]

E = deepcopy(W)

for delta in range(1,n):
  for j in range(n - delta):
    W[j, j + delta] = W[j, j + (delta - 1)] + P[j + delta]

def get_val(x,y,E):
  if x > y: return 0.0
  return E[x,y]

for delta in range(1,n):
  for i in range(n - delta):
    best, j =  infinity, i + delta
    # compute E[i, j]
    for r in range(i,j+1):
      nextE = get_val(i,r-1,E) + get_val(r+1,j,E) + W[i,j]
      if nextE < best:
        best = nextE
        C[i,j] = r
    E[i,j] = best

print(P)
print(W)
print(E)
print(C)
