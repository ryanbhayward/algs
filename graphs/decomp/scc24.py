# revised 2024 rbh, dfs now returns list of components
#   so scc is just components of dfs of transpose

def postorder(G, v, seen, L):
   seen[v] = True
   for nbr in G[v]:
     if not seen[nbr]:
       postorder(G, nbr, seen, L)
   L.append(v)

def dfs(D):
  seen = {v:False for v in D}
  C = [] # list of components
  # each component is a list of nodes, in postorder
  for v in D:
    if not seen[v]:
      L = []
      postorder(D, v, seen, L)
      C.append(L)
  return C

def transpose(D):
  T = {v:[] for v in D}
  for v in D: 
    for w in D[v]: 
      T[w].append(v)
  return T

def show(D):
  for v in D:
    print(v, ': ', end='')
    for w in D[v]:
      print(w, end=' ')
    print()

def scc(D):
   print('\ndigraph')
   show(D)
   T = transpose(D)
   print('\ntranspose')
   show(T)
   POT = dfs(T)
   print('\nstrongly connected components')
   for component in POT:
     for node in component:
        print(node, end='')
     print()

from graphs_input import D, D0, D2, D3, D4, D5, G
digraphs = [D, D0, D2, D3, D4, D5, G]
for d in digraphs:
  scc(d)
