# Prim's MST (simple version)
def infinity(): return 999

def indexOfMin(L,C):
  ndx = 0
  for j in range(1,len(L)):
    if C[L[j]] < C[L[ndx]]: ndx = j
  return ndx

def prim(G,source):
  cost, parent, fringe = {}, {}, []
  for v in G:
    cost[v], parent[v] = infinity(), -1
    fringe.append(v)
  cost[source],parent[source] = 0, source

  #doneEarly = False
  while len(fringe)>0:# and not doneEarly:
    u = fringe.pop(indexOfMin(fringe,cost))
    if u != source: print 'picked edge',u,parent[u]
    if cost[u] == infinity():  doneEarly = True
    for (v,costuv) in G[u]:
      if cost[v] > costuv: 
        cost[v] = costuv
        parent[v] = u
        #print 'to',v,'now',cost[v],'via',u

G = {'A': [['B',8],['C',8],['D',9],['E',13],['F',4],['G',11]],
     'B': [['A',8],['C',0],['D',9],['E',12],['F',1],['G',18]],
     'C': [['A',8],['B',0],['D',3],['E', 7],['F',15],['G', 6]],
     'D': [['A',9],['B',9],['C',3],['E', 1],['F',13],['G', 9]],
     'E': [['A',13],['B',12],['C',7],['D',1],['F',18],['G', 6]],
     'F': [['A',4],['B',1],['C',15],['D',13],['F',18],['G', 5]],
     'G': [['A',11],['B',18],['C',6],['D',9],['F',6],['G', 5]]}
prim(G,'A')
