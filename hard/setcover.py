#!/usr/local/bin/python3
from random    import randint
from itertools import chain, combinations
from copy      import deepcopy

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

def stringtoset(g,n):
  s = set()
  assert(n==len(g))
  for j in range(n):
    if g[j]=='*':
      s.add(j)
  return s

def gensubset(a,b,n): # subset of 0..n-1, each with prob a/b
  s = set()
  for j in range(n): 
    if randint(1,b) <= a: s.add(j)
  return s

def complete(L,n): # ensure union of L covers {0 .. n-1}
  u = set()
  for s in L: u = u.union(s)
  #print settostring(u,n)
  for j in range(n):
    if j not in u:
      r = randint(0,len(L)-1)
      L[r].add(j)
      #print 'add',j,'to',r

def mystr(j):
  if j > 9:
    return str(j)
  return ' ' + str(j)

def initsubsets(n,m,a,b): # m subs of 0..n-1
  # an element in a subset with probability a/b
  L = [] # list of subsets
  for _ in range(m): L.append(gensubset(a,b,n))
  complete(L,n)
  sumlen = 0
  print('\n   ',end='')
  for j in range(n):
    print('{0:2d}'.format(j), end='')
  print('')
  for j in range(len(L)):
    x = L[j]
    sumlen += len(x)
    print('S'+ mystr(j), settostring(x,n))
  print('\nuniverse { 0, 1, ...', n-1,'}')
  print('avg subset size', sumlen*1.0/m, '\n')
  return L

def greedy(n,m,L):
  # L list of m sets, universe {0 1 .. n-1}
  # return a greedy cover 
  casi = set()   # cover as set of indices, initially {}
  T = set(range(n))  # unsaturated elements
  while True:
    hits = [len(L[j].intersection(T)) for j in range(m)]
    best_index = hits.index(max(hits))
    casi.add(best_index)
    T = T - L[best_index]
    if T == set(): break
  print('greedy cover')
  for j in casi: 
    print('S' + mystr(j), settostring(L[j],n))

def bruteforce(n,m,L): 
  # L list of m sets, universe {0 1 .. n-1}
  set_indices = range(m) # [0 1 .. m-1]
  bestcover = ()
  for indexset in powerset(set_indices):
    subsetunion = set()
    for t in indexset: 
      subsetunion |= L[t]
    # indexsets sorted by cardinality, so first found is min
    if len(subsetunion) == n: 
      #print('size', len(indexset), 'cover', indexset,'\n')
      print('min cover')
      for j in indexset: 
        print('S' + mystr(j), settostring(L[j],n))
      return # so return once one is found


def example():
  L, n = [], 20
  ss = [
       '**-*----------*---**',
       '-*--*---*------*----',
       '-----*---***-*-----*',
       '--*-*-*----***------',
       '--*-*--------*------',
       '---*--*---------*--*',
       '----**-*------*-----',
       '---*--------**-*--*-',
       '-*------*-------**--',
       '------*------------*',
       '-------*--------*--*',
       '---*-*----*----**---',
       '---*----*-*-------*-',
       '*----------*-----*--',
       '-----*------**-*----']
  for x in ss:
    L.append(stringtoset(x,n))
  return L, n, len(L)

n,m,a,b = 40,15,1,5
L = initsubsets(n,m,a,b)
#L,n,m = example()
for myset in L:
  print(settostring(myset,n))
greedy(n,m,L)
bruteforce(n,m,L)
