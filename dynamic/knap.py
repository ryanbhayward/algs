from operator  import mul
from random    import randint
from itertools import chain, combinations

def genvector(n):
  v = [] 
  for j in range(n): v.append(randint(n,2*n))
  return v

def showRows(a,b,K): # last b-a rows
  print "..."
  for w in range(a,b):
    print w, ; print K[w]

def sack(n,W,K):  # given W, find 0/1 solution vector
  inSolution = [0 for j in xrange(n)]
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

def bruteforce(n,val,wt,W):
  indices = range(n) # [0 1 .. n-1]
  bestVal = 0
  for indexset in powerset(indices):
    v, w= 0, 0
    for t in indexset: 
      v+= val[t]
      w+= wt[t]
    if w <= W and v > bestVal: 
      bestVal = v
      print indexset, w, v

#python indexing: val[t],wt[t] corresponds to K[][t+1]
def solveknapsack(val,wt,W): 
  n = len(val)
  K = [[0 for j in xrange(n+1)] for w in xrange(W+1)]
  for j in range(1,n+1):
    for w in range(W+1):
      if wt[j-1]>w: K[w][j] = K[w][j-1]
      else: K[w][j] = max(K[w][j-1], K[w-wt[j-1]][j-1]+val[j-1])
  lastfew = 30
  showRows(max(W+1-lastfew,0),W+1,K) # print last few rows of K
  solvec = sack(n,W,K)
  print '\n', sum(map(mul, solvec, wt)), solvec, sum(map(mul, solvec, val))
    
#n = 25
#W, val, wt = (n*n*3)/4, genvector(n), genvector(n)
n,W,val,wt =  6, 27, [6, 9, 7, 9, 8, 7], [11, 6, 8, 10, 8, 9]
print 'val  ', ; print(val)
print 'wt   ', ; print(wt)
print 'max value knapsack with weight at most', W, '?'
solveknapsack(val,wt,W)
#bruteforce(n,val,wt,W)
