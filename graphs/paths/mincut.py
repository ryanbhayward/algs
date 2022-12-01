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

#edgeTuple = ((0,1), (0,2), (1,2), (2,3), (3,4), (3,5), (4,5))
edgeTuple = ((0,1),(0,2),(1,2),(1,3),(2,3),(2,4),(3,5),(4,5),(4,6),(5,6),(5,7),(6,7))
n, m = 8, len(edgeTuple)

from numpy.random import default_rng

def randomcut(n, edges):
  assert(n>2)
  rng = default_rng()
  myperm = np.arange(m)
  rng.shuffle(myperm)
  #print(myperm)

  parents, components = np.arange(n), n

  for j in range(m):
    edge = edges[myperm[j]]
    c0, c1 = myfind(edge[0], parents), myfind(edge[1], parents)
    if c0 != c1:
      parents[c0] = c1
      components -= 1
      if components == 2: break

  #print(parents)
  #comp0, root0 = [0], myfind(0, parents)
  #for j in range(1, n):
  #  if myfind(j, parents) == root0:
  #    comp0.append(j)
  #print(comp0)

  cutEdges = []
  for e in edges:
    if myfind(e[0], parents) != myfind(e[1], parents):
      cutEdges.append(e)
  return cutEdges


trials, wins = 10, 0
mincutsize = 2
for _ in range(trials):
  cut = randomcut(n, edgeTuple)
  c = len(cut)
  #mymin = min(mymin, c)
  if c == mincutsize: 
    wins += 1
    print(cut)
print(wins, 'wins after', trials, 'trials')
