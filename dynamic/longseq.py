import random  # longest increasing subsequence

def genseq(n):
  S = []
  #for _ in range(n): S.append(random.randint(1,n))
  #return S
  for j in range(n): 
    S.append(j)
  random.shuffle(S)
  return S

def longest(S):
  # define f(t): length of longest increasing subsequence
  #   of S[0 ... t] that includes S[t]
  L= [1] # initialize L[0] to f(0)
  for k in range(1,len(S)):
    mymax = 0  # L entries positive, so this init ok
    # for t in {0 ... k-1}, L[t] = f(t)
    for j in range(k):
      if S[j]<S[k]: mymax = max(mymax,L[j])
    L.append(1+mymax)
  # L[k] = f(k) 
  return L
  # for t in {0 ... n-1},  where n = len(S),
  #   L[t] = f(t) 

def pretty(S):
  print "[",
  for j in S:
    print '%2d' % j, 
  print "]"

#S = [7,10,6,2,4,8,9,3,2,7,9,1]
#S = [1,9,7,2,3,9,8,4,2,6,10,7]
#S = [8,3,2,7,4,9,1,11,5]; print S
S = genseq(20); pretty(S); print ""
L = longest(S); pretty(L)
