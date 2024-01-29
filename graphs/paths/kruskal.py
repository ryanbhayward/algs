# simple Kruskal mst
import weighted, UF

# convert from weighted adjacency list 
#         to tuple list:   (v,w,wt_vw)
def createEdgeList(G):
  L = []
  for v in G:
    for (w,wt) in G[v]:
      if ord(v)<ord(w): L.append((v,w,wt))
  return L

# extract tuple with min wt
def extractmin(L):
  ndxMin, valMin = 0, L[0][2]
  for j in range(1,len(L)):
    t = L[j]
    if t[2] < valMin:
      ndxMin, valMin = j, t[2]
  return L.pop(ndxMin)

def kruskalDemo(G):
  L = createEdgeList(G)
  parent = {}
  for v in G: parent[v] = v

  while len(L) > 0:
    t = extractmin(L)
    a, b = t[0], t[1]
    ra, rb = UF.myfind(a,parent), UF.myfind(b,parent)
    #print a, ra, b, rb,
    if ra != rb:
      #print 'add edge',a,b,t[2]
      print(a,b,t[2])
      UF.myunion(ra,rb,parent)
    #else: print 'reject  ',a,b

kruskalDemo(weighted.G6)
