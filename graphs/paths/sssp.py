# simple Dijkstra 
import weighted
def sssp(G,source):
  infinity = weighted.infinity(G)
  dist, parent, fringe = {}, {}, []
  for v in G:
    dist[v], parent[v] = infinity, -1
    fringe.append(v)
  dist[source],parent[source] = 0, source

  while len(fringe)>0:
    u = fringe.pop(weighted.indexOfMin(fringe,dist))
    for (v,duv) in G[u]:
      if (v in fringe) and (dist[v] > dist[u] + duv): 
        dist[v] = dist[u] + duv
        parent[v] = u
        print 'to',v,'now',dist[v],'via',u

  print 'from',source,': ',
  for v in sorted(G): print v,
  print '\ndistance ',
  for v in sorted(G): print dist[v],
  print '\nparent   ',
  for v in sorted(G): print parent[v],

G = weighted.G2
sssp(G,'A')
