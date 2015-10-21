# single source shortest path 
# for graphs/digraphs with non-negative edge weights
# (simple implementation: no priority queue)
def weightSum(G):
  sum = 0
  for u in G: 
    for (v,weight) in G[u]: sum += weight
  return sum

def showAll(G,D,P):
  print '    ',
  for v in sorted(G): print v,
  print '\ndist',
  for v in sorted(G): print D[v],
  print '\nprnt',
  for v in sorted(G): print P[v],
  print ''

def show(G,F,D):
  for v in sorted(F): print v,D[v],' ',
  print ''

def sssp(G,source):
  infinity = 999 + weightSum(G)
  dist, parent, fringe = {}, {}, []
  for v in G:
    dist[v], parent[v] = infinity, -1
    fringe.append(v)
  dist[source],parent[source] = 0, source

  doneEarly = False
  print '\nsource node:',source,'\n'
  while len(fringe)>0 and not doneEarly:
    ndxMin = 0
    for j in range(1,len(fringe)):
      if dist[fringe[j]] < dist[fringe[ndxMin]]: ndxMin = j
    u = fringe[ndxMin]
    show(G,fringe,dist)
    print 'final distance:',u,dist[u],'\n'
    fringe.pop(ndxMin)
    if (dist[u] == infinity):  doneEarly = True
    for (v,duv) in G[u]:
      if dist[v] > dist[u] + duv: 
        dist[v] = dist[u] + duv
        parent[v] = u
        print '  ',v,dist[v],'via',u
  showAll(G,dist,parent)

G = {'A': [['B',4],['C',2]],
     'B': [['C',3],['D',2],['E',3]],
     'C': [['B',1],['D',4],['E',5]],
     'D': [],
     'E': [['D',1]]}
G2 = {'A': [['B',8],['C',8],['D',9],['E',13],['F',4],['G',11]],
     'B': [['A',8],['C',0],['D',9],['E',12],['F',1],['G',18]],
     'C': [['A',8],['B',0],['D',3],['E', 7],['F',15],['G', 6]],
     'D': [['A',9],['B',9],['C',3],['E', 1],['F',13],['G', 9]],
     'E': [['A',13],['B',12],['C',7],['D',1],['F',18],['G', 6]],
     'F': [['A',4],['B',1],['C',15],['D',13],['F',18],['G', 5]],
     'G': [['A',11],['B',18],['C',6],['D',9],['F',6],['G', 5]]}
sssp(G,'A')
