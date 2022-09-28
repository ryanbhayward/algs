#!/usr/bin/python
from operator  import mul
from random    import randint
from itertools import chain, combinations

def genvector(n):
  v = [] 
  for j in range(n): v.append(randint(n,2*n))
  return v

def showRows(a,b,K,inf): # rows a .. b-1
  for w in range(a,b): #inf printed as '-'
    print('%4d'%w, end='')
    for k in K[w]:
      if k==inf: print('  -', end='')
      else: print('%4d'%k, end='')
    print('')

def sack(n,W,K):  # given W, find 0/1 solution vector
  inSolution = [0 for j in range(n)]
  ndx,w  = n,W
  while (w>0) and (ndx>0):
    while (ndx>0) and (K[w][ndx]==K[w][ndx-1]):
      ndx-=1
    if (ndx>0):
      ndx -= 1
      inSolution[ndx] = 1
      w -= wt[ndx]
  return inSolution

def powerset(iterable):
#https://docs.python.org/2/library/itertools.html#recipes
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def knapBF(val,wt,W): # brute force knapsack
  indices = range(len(val)) # [0 1 .. n-1]
  bestVal = 0
  print('knapBF')
  print('subset    wt val   max wt',W)
  for indexset in powerset(indices):
    v = sum( val[t] for t in indexset )
    w = sum(  wt[t] for t in indexset )
    if w <= W and v > bestVal: 
      bestVal = v
      print(indexset, w,v)

def knapDP(val,wt,W): #usual dyn. prog. knap, by weight
# K[w][j]  will be best value knapsack, weight at most w, 
#         using subset of { item_1, item_2, ..., item_j }
# warning: K[][] needs an extra 0th column, so its indices
#   are off-by-one w.r.t. val[], wt[]
# eg. val[v], wt[t]  refer to t+1'st item
#     also K[][t+1]  refers to t+1'st item
#
  print('knapDP')
  n = len(val)
  K = [[0 for j in range(n+1)] for w in range(W+1)]
  for j in range(1,n+1):
    for w in range(W+1):
      K[w][j] = K[w][j-1] if w < wt[j-1] \
        else max(K[w][j-1], K[w-wt[j-1]][j-1] + val[j-1])
  lastfew = 100  # show last few rows of computation
  showRows(max(W+1-lastfew,0),W+1,K,1+sum(wt)) # print last few rows of K
  solvec = sack(n,W,K)
  print('\n', sum(map(mul, solvec, wt)), solvec, sum(map(mul, solvec, val)),'\n')
    
def knapDPV(val,wt,V): #dynamic programming by value
  # A[v][j] is min weight of subset of items 0..j with exact val v
  infinity = 1 + sum(val) #larger than any possible sum of values
  n = len(val)
  A = [[infinity for j in range(n)] for v in range(V+1)]
  for j in range(n): A[0][j] = 0
  A[val[0]][0] = wt[0]  # end initialization
  for v in range(1,V+1):  # row    0 already initialized
    for j in range(1,n):  # column 0 "       "
      A[v][j] = A[v][j-1] if v < val[j] \
        else min(A[v][j-1], A[v - val[j]][j-1] + wt[j])
  showRows(0,len(A),A,infinity)

n = 6
W, val, wt = (n*n*3)/4, genvector(n), genvector(n)
#n,W,val,wt =  6, 27, [6, 9, 7, 9, 8, 7], [11, 6, 8, 10, 8, 9]
#n,W,val,wt = 5, 23, [7, 6, 10, 6, 9], [5, 8, 10, 8, 5]
#n,W,val,wt = 5, 18, [5, 8, 10, 7, 6], [4, 7, 9, 6, 5]
#n,W,val,wt = 4, 13, [10, 9, 8, 6], [8, 7, 6, 5]
n,W,val,wt = 4, 5, [3, 1, 2, 2], [2 , 1, 1, 3]
#knapBF(val,wt,W)
knapDP(val,wt,W)
#knapDPV(val,wt,sum(val))
print('val', val)
print('wt ', wt) 
print('W ', W)
