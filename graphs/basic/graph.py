def dfs(G):
  pre,post,seen,cmpt = {},{},{},{}
  for v in G: 
    seen[v] = False
  clock, cnum  = [0], 0 #clock[0] passed by ref
  for v in sorted(G):
    if not seen[v]:
      cnum += 1
      explore(G,v,seen,pre,post,clock,cmpt,cnum)
  showall(G,pre,post,cmpt)

def explore(G,v,seen,pre,post,clock,cmpt,c):
  seen[v] = True
  cmpt[v] = c
  timestamp(v, pre, clock)
  for nbr in G[v]:
    if not seen[nbr]:
      explore(G,nbr,seen,pre,post,clock,cmpt,c)
  timestamp(v, post, clock)

def timestamp(v, order, clock):
  clock[0]+= 1; order[v] = clock[0]

def showall(G,pre,post,cnum):
  print '     ',
  for v in sorted(G): print '%2s' % v,
  print '\npre  ',
  for v in sorted(G): print '%2s' % pre[v],
  print '\npost ',
  for v in sorted(G): print '%2s' % post[v],
  print '\ncmpt ',
  for v in sorted(G): print '%2s' % cnum[v],
  
def show(G):
  for v in sorted(G):
    print v,':',
    for j in G[v]: print j,
    print ''
  print ''

#G = {'A': ['C', 'E', 'F'],
     #'B': ['D', 'G'],
     #'C': ['A', 'F'],
     #'D': ['B', 'G'],
     #'E': ['A', 'F'],
     #'F': ['A', 'C', 'E'],
     #'G': ['B', 'D'],
     #'H': []}
G = {'A': ['F'],
     'B': ['C','D'],
     'C': ['B','D','E','G'],
     'D': ['B','C','G'],
     'E': ['C'],
     'F': ['A'],
     'G': ['C', 'D']}

show(G)
dfs(G)
