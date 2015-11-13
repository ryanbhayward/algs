from random    import randint
from itertools import chain, combinations

def powerset(iterable):
#https://docs.python.org/2/library/itertools.html#recipes
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def settostring(s,n): # set as pretty binary string
  x = ''
  for j in range(n):
    if j in s:   x += ' *'
    else:        x += ' -'
  return x

def gensubset(a,b,n): # subset of 0..n-1, each with prob a/b
  s = set()
  for j in range(n): 
    if randint(1,b) <= a: s.add(j)
  return s

def initsubsets(n,m,a,b): # m subs of 0..n-1
  # an element in a subset with probability a/b
  L = [] # list of subsets
  for _ in range(m): L.append(gensubset(a,b,n))
  sumlen = 0
  for x in L:
    sumlen += len(x)
    print settostring(x,n)
  print 'universe size', n,' avg subset size', sumlen*1.0/m
  return L

def bruteforce(n,m,L):
  indices = range(m) # [0 1 .. m-1]
  bestcover = ()
  for indexset in powerset(indices):
    subsetunion = set()
    for t in indexset: 
      subsetunion |= L[t]
    # indexsets sorted by cardinality, so first found is min
    if len(subsetunion) == n: 
      print 'size', len(indexset), 'cover', indexset
      for j in indexset: print settostring(L[j],n)
      return # so return once one is found

n,m,a,b = 40,25,2,11
L = initsubsets(n,m,a,b)
bruteforce(n,m,L)
