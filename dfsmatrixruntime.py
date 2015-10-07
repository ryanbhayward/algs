def n(G): return len(G[0])
def alpha(j): return chr(j+ord('A'))

def traverse(G):
  seen,cmpt,cnum,work = {},{},0,[0]
  for v in range(n(G)):
    seen[v] = False
    cmpt[v] = 0
  for v in range(n(G)):
    work[0] += 1
    if not seen[v]:
      cnum += 1
      dfs(G,v,seen,cmpt,cnum,work)
  print ''
  for v in range(n(G)): print alpha(v),
  print ''
  for v in range(n(G)): print cmpt[v],
  print '\nwork', work[0]

def dfs(G,v,seen,cmpt,c,work):
  seen[v],cmpt[v],work[0] = True,c,work[0]+1
  for j in range(n(G)):  # possible nbr
    work[0] += 1
    if G[v][j]==1:     # j is nbr
      if not seen[j]:
        dfs(G,j,seen,cmpt,c,work)
  print alpha(v),

def show(G):
  print '   ',
  for v in range(n(G)): print alpha(v),
  print ''
  for v in range(n(G)):
    print alpha(v),':',
    for w in range(n(G)):
      if G[v][w]==1: print '1',
      else:          print '0',
    print ''
  print ''

G = ([0, 0, 0, 0, 0, 1, 0],
     [0, 0, 1, 1, 0, 0, 0],
     [0, 1, 0, 1, 1, 0, 1],
     [0, 1, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 1, 0, 0, 0])

show(G)
traverse(G)
