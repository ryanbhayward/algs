def traverse(G):
  seen,cmpt,cnum,work = {},{},0,[0]
  for v in G: 
    seen[v] = False
    cmpt[v] = 0
  for v in reversed(sorted(G)):
    work[0] += 1
    if not seen[v]:
      cnum += 1
      dfs(G,v,seen,cmpt,cnum,work)
  print ''
  for v in sorted(G): print v, 
  print ''
  for v in sorted(G): print cmpt[v],
  print '\nwork', work[0]

def dfs(G,v,seen,cmpt,c,work):
  seen[v],cmpt[v],work[0] = True,c,work[0]+1
  for nbr in reversed(sorted(G[v])):
    work[0] += 1
    if not seen[nbr]:
      dfs(G,nbr,seen,cmpt,c,work)
  print v,

def show(G):
  for v in sorted(G):
    print v,':',
    for j in G[v]: print j,
    print ''
  print ''

#G = {'A': ['B','E'],
     #'B': ['A'],
     #'C': ['D','G','H'],
     #'D': ['C','H'],
     #'E': ['A','I','J'],
     #'F': [],
     #'G': ['C','H','K'],
     #'H': ['C','D','G','K'],
     #'I': ['E','J'],
     #'J': ['E','I'],
     #'K': ['G','H'],
     #'L': ['H'] }
G = {'A':['C'], 'B':['D','G','J'], 'C':[], 'D':['C','F'],
     'E':['C','F'], 'F':[], 'G':['F'], 'H':['B','J'],
     'I':['A','B','J'], 'J':[]}

#show(G)
traverse(G)
