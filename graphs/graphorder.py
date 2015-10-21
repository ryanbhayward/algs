def printorder(G):
  seen = {} 
  for v in G: seen[v] = False
  for v in G:
    if not seen[v]:
      explore(G,v,seen)
      print ''

def printbfs(G):
  seen = {}
  for v in G: 
    seen[v] = False
  for v in sorted(G):
    if not seen[v]:
      explorebfs(G,v,seen)
      print ''

def printstackdfs(G):
  seen = {}
  for v in G: 
    seen[v] = False
  for v in sorted(G):
    if not seen[v]:
      print ''
      explorestackdfs(G,v,seen)

def explore(G,v,seen):
  seen[v] = True
  print v,
  for nbr in G[v]:
    if not seen[nbr]:
      explore(G,nbr,seen)
  print v,

def addtolist(L,v,seen):
  L.append(v); seen[v]=True

def explorebfs(G,v,seen):
  # here: seen when pushed
  Q = []
  addtolist(Q,v,seen)
  while len(Q)>0:
    v = Q.pop(0); print v, 
    for nbr in G[v]:
      if not seen[nbr]: 
        addtolist(Q,nbr,seen)

def explorestackdfs(G,v,seen):
  # here: seen when popped
  S = [v]
  while len(S)>0:
    v = S.pop()
    if not seen[v]:
      seen[v] = True; print v,
    for nbr in reversed(G[v]):
      if not seen[nbr]: 
        S.append(nbr)

def show(G):
  for v in sorted(G):
    print v,':',
    for j in G[v]: print j,
    print ''

#G = {'A': ['C', 'E', 'F'],
     #'B': ['D', 'G'],
     #'C': ['A', 'F'],
     #'D': ['B', 'G'],
     #'E': ['A', 'F'],
     #'F': ['A', 'C', 'E'],
     #'G': ['B', 'D'],
     #'H': []}
#G = {'A': ['F'],
     #'B': ['C','D'],
     #'C': ['B','E','H'],
     #'D': ['B'],
     #'E': ['C','G','H'],
     #'F': ['A'],
     #'G': ['E'],
     #'H': ['C','E']}
#G = {'A': ['B','C'],
     #'B': ['A'],
     #'C': ['A']}
G = {'A':['E','I'], 'B':[], 'C':['D','E','F'], 'D':['H'], 'E':['G'],
     'F':['C','D'], 'G':['B','C'], 'H':['B','F'], 'I':['A','D']}
     
show(G) 
printorder(G); print ''
#show(G)
#printbfs(G); print ''
#show(G)
#printstackdfs(G)
#show(G)
