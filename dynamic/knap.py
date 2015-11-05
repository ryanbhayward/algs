import random, operator
def genvector(n):  
  v = [] 
  for j in range(n): v.append(random.randint(n,2*n))
  return v

def showRows(a,b,K): # last b-a rows
  print "..."
  for w in range(a,b):
    print w, ; print K[w]

def sack(n,W,K):  # get 0/1 solution vector
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

#python indexing:  val[t],wt[t] corresponds to K[t+1]
def solveknapsack(val,wt,W): 
  n = len(val)
  K = [[0 for j in xrange(n+1)] for w in xrange(W+1)]
  for j in range(1,n+1):
    for w in range(W+1):
      if wt[j-1]>w: K[w][j] = K[w][j-1]
      else: K[w][j] = max(K[w][j-1], K[w-wt[j-1]][j-1]+val[j-1])
  lastfew = 25   
  showRows(W+1-lastfew,W+1,K) # print last few rows of K
  solvec = sack(n,W,K)
  print sum(map(operator.mul, solvec, val)), solvec
    
n = 10
W = (n*n*3)/4
val,wt = genvector(n),genvector(n)
print 'val  ', ; print(val)
print 'wt   ', ; print(wt)
solveknapsack(val,wt,W)
