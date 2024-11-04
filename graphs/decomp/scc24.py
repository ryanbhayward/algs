# revised 2024 rbh, dfs now returns list of components
#   so scc is just components of dfs of transpose

def dfs_postorder(G, v, seen, L):
   seen[v] = True
   for nbr in G[v]:
     if not seen[nbr]:
       dfs_postorder(G, nbr, seen, L)
   L.append(v)

def node_list(D):
  L = [v for v in D]
  return L

def get_nodes(C):
   L = []
   for component in C:
     for node in component:
       L.append(node)
   return L

def dfs(D, nodes):
  seen = {v:False for v in D}
  C = [] # list of components
  # each component is a list of nodes, in postorder
  for v in nodes:
    if not seen[v]:
      L = []
      dfs_postorder(D, v, seen, L)
      C.append(L)
  return C

def transpose(D):
  T = {v:[] for v in D}
  for v in D: 
    for w in D[v]: 
      T[w].append(v)
  return T

def show_graph(D):
  for v in D:
    print(v, ': ', end='')
    for w in D[v]:
      print(w, end=' ')
    print()

def show(sccs):
   print('\nstrongly connected components')
   for component in sccs: 
     for node in component:
        print(node, end='')
     print()

def scc(D):
   T = transpose(D)
   PO = get_nodes(dfs(T, node_list(T)))
   PO.reverse()
   sccs = dfs(D, PO)
   show(sccs)

def scc2(D): # this doesn't always work: try it on D6
   PO = get_nodes(dfs(D, node_list(D)))
   sccs = dfs(D, PO)
   show(sccs)

from graphs_input import D, D0, D1, D2, D3, D4, D5, D6, G
#for d in [D, D0, D1, D2, D3, D4, D5, D6, G]:
for d in [D6]:
  print('\nnext digraph')
  show_graph(d)
  scc(d)
  scc2(d)
