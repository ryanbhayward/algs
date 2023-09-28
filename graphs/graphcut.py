# randomized min cut using mst parent array
import random

def myfind(x, parents):
  while x!=parents[x]: x = parents[x]
  return x

def myunion(x,y,parents): parents[x] = y

def nodeedgecount(G):
  n,m = 0,0
  for v in G:
    n+= 1
    for w in G[v]:
      if v < w: m+= 1
  return n,m

def edgelist(G):
  L = []
  for v in G:
    for w in G[v]: 
      if v < w: L.append((v,w))
  return L

def cutedges(E,P):
  edgeset = []
  for e in E:
    if myfind(e[0],P) != myfind(e[1],P):
      edgeset.append(e)
  return edgeset

#add clique {a,a+1,...b_1} to G
def addclique(a,b,G):
  for j in range(a,b-1):
    for k in range(j+1,b):
      G[j].append(k)
      G[k].append(j)

def samplegraph(n):
  G = {}
  for v in range(n):
    G.update({v:[]})
  addclique(0,n//2,G)
  addclique(n//2,n,G)
  for j in range(n//2-1):
    G[j].append(j+n//2)
    G[j+n//2].append(j)
  return G

def randomgraph(n):
  G = {}
  for v in range(n):
    G.update({v:[]})
  for v in range(n-1):
    for w in range(v+1,n):
      if random.randint(0,1)==1:
        G[v].append(w)
        G[w].append(v)
  return G

def makeparents(G):
  p = []
  for v in sorted(G):
    p.append(v)
  return p

def randomcut(G,n,E):
  edgesadded = 0
  P = makeparents(G)
  random.shuffle(E)
  for e in E:
    x = myfind(e[0],P)
    y = myfind(e[1],P)
    if x != y:
      myunion(x,y,P)
      edgesadded += 1
      if edgesadded == n-2:
        return cutedges(E,P)

def showgoodcuts(G,t,printEdges):
# iterate t times; show cut every time it improves
  n,m = nodeedgecount(G)
  E = edgelist(G)
  bestcutsize = m+1 # initialize with impossible value
  for j in range(t):
    C = randomcut(G,n,E)
    if len(C) < bestcutsize: 
      bestcut = C
      bestcutsize = len(bestcut)
      print('try',j,': size',len(bestcut))
      if printEdges: print(bestcut)
  print('')

G = {0:[1,2,3],
     1:[0,2,3],
     2:[0,1,3,4],
     3:[0,1,2,5],
     4:[2,5,6,7],
     5:[3,4,6,7],
     6:[4,5,7],
     7:[4,5,6]
}
     
showgoodcuts(G,10,True)
H = samplegraph(12)
showgoodcuts(H,10,False)
H = randomgraph(200)
showgoodcuts(H,200,False)
