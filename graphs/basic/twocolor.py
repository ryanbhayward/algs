# return two coloring or odd cycle
# RBH 2019

def twocol(G): 
  show(G)
  color, parent = {}, {}
  for v in G: color[v] = 0
  for v in sorted(G):
    if 0 == color[v]: 
      if not bfscol(G, v, color, parent): return
  print('\n            ', end='')
  for v in sorted(G): print(v, end = ' ')
  print('\n2-coloring ', end=' ')
  for v in sorted(G): print(color[v], end = ' ')
  #print('\nparent', end=' ')
  #for v in sorted(G): print(parent[v], end = ' ')
  print('\n')

def lineprint(L):
  for j in range(len(L)):
    print(L[j], end = ' ')

def pathToRoot(v, par):
  L = [v]
  while par[v] != v:
    pv = par[v]
    L.append(pv)
    v = pv
  return L

def show_cycle(G, v, w, parent):
  L = pathToRoot(v, parent)
  L.reverse()
  M = pathToRoot(w, parent)
  M.pop()
  print('\ncycle', end=' ')
  lineprint(L)
  lineprint(M)
  print('\n')

def bfscol(G, v, color, parent):
  Q = [v]
  color[v], parent[v] =  1, v
  while len(Q) > 0:
    v = Q.pop(0)
    for nbr in G[v]:
      if color[nbr] == 0:
        color[nbr], parent[nbr] = 3 - color[v], v
        Q.append(nbr)
      elif color[nbr] == color[v]:
        show_cycle(G, v, nbr, parent)
        return False
      # else nbr already has a color, but it's different from v, so ok
  return True

def show(G):
  print()
  for v in sorted(G):
    print(v+':', end=' ')
    for j in G[v]: print(j, end=' ')
    print()

G  = {'A':['B','C'], 'B':['A','C'], 'C':['A','B']}
G2 = {'A':['B','C'], 'B':['A','D'], 'C':['A','D'], 'D':['B','C']}
G3 = {'A':['B','E'], 'B':['A','C'], 'C':['B','D'], 'D':['C','E'], 'E':['D','A']}

for g in [G, G2, G3]: twocol(g)
