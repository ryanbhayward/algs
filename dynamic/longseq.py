import random  # longest increasing subsequence

def pretty(S): # print vector, uniform field width
  print "[",
  for j in S:
    print '%2d' % j, 
  print "]"

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
#              of S[0 ... t] that includes S[t]
  L = [1] # L[0] = f(0)
  for k in range(1,len(S)):
    # invariant: for t in {0 ... k-1}, L[t] = f(t)
    sofar = 0  
    for j in range(k):
      # sofar = max{ all i in {0 .. j-1} with S[i] < S[k]: f(i) }
      if S[j]<S[k]: sofar = max(sofar,L[j])
    # sofar = max { all j in {0 .. k-1} with S[j] < S[k]: f(j) }
    L.append(1+sofar)
    pretty(L)
    # L[k] = f(k)
  # for n = len(S), for all t in {0 ... n-1}: L[t] = f(t) 
  return L

#S = [7,10,6,2,4,8,9,3,2,7,9,1]
#S = [1,9,7,2,3,9,8,4,2,6,10,7]
#S = [8,3,2,7,4,9,1,11,5]; print S
S = genseq(20); pretty(S); print ""
L = longest(S)
