# simple Prim MST from source vertex
# for graphs/digraphs with non-negative edge weights
# (simple implementation: no priority queue)
import weighted

def primMst(G,start):
  infinity = weighted.infinity(G)
  cost, parent, fringe = {}, {}, []
  for v in G:
    cost[v], parent[v] = infinity, -1
    fringe.append(v)
  cost[start],parent[start] = 0, start

  doneEarly = False
  while len(fringe)>0 and not doneEarly:
    weighted.showFringe(G,fringe,cost,infinity)
    u = fringe.pop(weighted.indexOfMin(fringe,cost))
    print '\npick',u,':',
    if (cost[u] == infinity): doneEarly = True
    for (v,duv) in G[u]:
      if (v in fringe) and (cost[v] > duv):
        cost[v] = duv
        parent[v] = u
        print v,cost[v],' ',
    print ''
  weighted.showAll(G,cost,parent)
  print 'mst weight', sum(cost.values())

G = weighted.G4
primMst(G,'A')
