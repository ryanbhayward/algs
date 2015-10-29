# Prim's MST (simple version)
import weighted 

def prim(G,source):
  cost, parent, fringe = {}, {}, []
  infin = weighted.infinity(G)
  for v in G:
    cost[v], parent[v] = infin, -1
    fringe.append(v)
  cost[source],parent[source] = 0, source

  #doneEarly = False
  sum = 0
  print source, 'start'
  while len(fringe)>0:# and not doneEarly:
    u = fringe.pop(weighted.indexOfMin(fringe,cost))
    sum += cost[u]
    if u != source: print u,parent[u],cost[u]
    if cost[u] == infin:  doneEarly = True
    for (v,costuv) in G[u]:
      if (v in fringe) and (cost[v] > costuv): 
        cost[v] = costuv
        parent[v] = u
  print 'mst weight', sum

G = weighted.G4
for v in G:
  prim(G,v)
  print ''
