def traverse(G):
  seen,cmpt,cnum,work = {},{},0,[0] #work reflects runtime
  for v in G:
    seen[v] = False
    cmpt[v] = 0
  for v in sorted(G):
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
  for nbr in sorted(G[v]):
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

G = {'A': ['F'],
     'B': ['D','C'],
     'C': ['G','B','E','D'],
     'D': ['G','B','C'],
     'E': ['C','G'],
     'F': ['A'],
     'G': ['C', 'D']}

show(G)
traverse(G)
