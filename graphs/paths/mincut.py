# randomized Kruskal min cut algorithm,
#   similar to Karger's      rbh 2022

import numpy as np

def myfind(v,P): # simple find
  while P[v] != v:
    v = P[v]
  return v

def findGP(x, parents): # find, gp compress
  px = parents[x]
  if x==px: 
    return x
  gx = parents[px] # grandparent
  while px != gx:
    parents[x] = gx
    x = px 
    px = gx 
    gx = parents[gx]
  return px

def myunion(x,y,P): # simple union
  rootx, rooty = myfind(x,P), myfind(y,P)
  P[rootx] = rooty

edgeSet = ((0,1), (0,2), (1,2), (2,3), (3,4), (4,5), (4,6), (5,6))
n, m = 7, len(edgeSet)
parents = np.fromiter(range(n), dtype= 'int8')
print(parents)
for j in range(n):
  print(parents[j])
for e in edgeSet:
  print(e)

