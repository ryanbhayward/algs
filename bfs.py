def bfs(G): # depth in bfs forest
  seen, depth = {}, {}
  for v in G: 
    seen[v], depth[v] = False, 0
  print 'bfs order       ',
  for v in sorted(G):
    if not seen[v]:
      explorebfs(G,v,seen,depth)
  print '\nnodes           ',
  for v in sorted(G): print v,
  print '\nbfs forest depth',
  for v in sorted(G): print depth[v],
  print ''

def addtolist(L,v,seen):
  L.append(v); seen[v]=True

def explorebfs(G,v,seen,d):
  Q = []
  addtolist(Q,v,seen)
  while len(Q)>0:
    v = Q.pop(0); print v,
    for nbr in G[v]:
      if not seen[nbr]:
        d[nbr] = 1 + d[v]
        addtolist(Q,nbr,seen)

def show(G):
  for v in sorted(G):
    print v,':',
    for j in G[v]: print j,
    print ''

#G = {'A': ['F'],
     #'B': ['C','D'],
     #'C': ['B','E','H'],
     #'D': ['B'],
     #'E': ['C','G','H'],
     #'F': ['A'],
     #'G': ['E'],
     #'H': ['C','E']}
G = {
'A':['H'],
'B':['I','L'],
'C':['E','I','J'],
'D':['F'],
'E':['C','G','I','J','L'],
'F':['D','J'],
'G':['E','L'],
'H':['A','K','M'],
'I':['B','C','E','L'],
'J':['C','E','F'],
'K':['H'],
'L':['B','E','G','I'],
'M':['H'],
}

show(G)
bfs(G)
