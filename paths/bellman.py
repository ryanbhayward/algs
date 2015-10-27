# bellman ford
def infinity(): return 999
def myprint(d):
  if d==infinity(): print '--',
  else: print '%2s' % d,

def update(x,y,dxy,D,P):
  change = 0
  if D[x]<infinity() and D[y] > D[x] + dxy:
    D[y], P[y], change = D[x] + dxy, x, 1
  return change

def sssp(G,source):
  dist, parent = {}, {}
  for v in G:
    dist[v], parent[v] = infinity(), -1
  dist[source],parent[source] = 0, source

  print 'from',source,'  ',
  for v in sorted(G): print '%2s' % v,
  print '\ndistance ',
  for v in sorted(G): myprint(dist[v])

  for _ in range(len(G)-1):
    updates = 0 
    for v in sorted(G):
      for (w,dvw) in sorted(G[v]):
        updates += update(v,w,dvw,dist,parent)
    print '\ndistance ',
    for v in sorted(G): myprint(dist[v])
    if updates==0: break

  print '\nparent   ',
  for v in sorted(G): print '%2s' % parent[v],
  print ''

G = {'A': [['C',2],['D',7],['F',1]],
     'B': [['D',1],['E',-2],['F',3]],
     'C': [['A',2],['E',1],['F',4]],
     'D': [['A',7],['B',-1],['F',3]],
     'E': [['B',3],['C',1],['F',6]],
     'F': [['A',1],['B',3],['C',4],['D',-2],['E',6]]}
     #'E': [['B',-2]],
     #'F': [['A',-4],['E',-1]],
#G = {'S': [['A',1]],
     #'A': [['B',1]],
     #'B': [['S',-3]]}
#G = {'A': [['E',2]],
     #'B': [['A',1],['C',1]],
     #'C': [['D',3]],
     #'D': [['E',-1]],
     #'E': [['B',-2]],
     #'F': [['A',-4],['E',-1]],
     #'G': [['F',1]],
     #'S': [['A',10],['G',8]]}
sssp(G,'A')
