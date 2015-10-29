# single source shortest path  (source means start)
# for graphs/digraphs with non-negative edge weights
# (simple implementation: no priority queue)
import weighted

def sssp(G,start):
  infinity = weighted.infinity(G)
  dist, parent, fringe = {}, {}, []
  for v in G:
    dist[v], parent[v] = infinity, -1
    fringe.append(v)
  dist[start],parent[start] = 0, start

  doneEarly = False
  while len(fringe)>0 and not doneEarly:
    weighted.showFringe(G,fringe,dist,infinity)
    u = fringe.pop(weighted.indexOfMin(fringe,dist))
    print '\npick',u,':',
    if (dist[u] == infinity): doneEarly = True
    for (v,duv) in G[u]:
      if (v in fringe) and (dist[v] > dist[u] + duv): 
        dist[v] = dist[u] + duv
        parent[v] = u
        print v,dist[v],' ',
    print ''
  weighted.showAll(G,dist,parent)

G = weighted.G
sssp(G,'A')
