# used for weighted graphs
def weightSum(G):
  sum = 0
  for u in G: 
    for (v,weight) in G[u]: sum += weight
  return sum

def infinity(G): return 999+weightSum(G)

def indexOfMin(L,C):
  ndx = 0
  for j in range(1,len(L)):
    if C[L[j]] < C[L[ndx]]: ndx = j
  return ndx

def showAll(G,D,P):
  print '\nprnt',
  for v in sorted(G): print P[v],
  print '\nnode',
  for v in sorted(G): print v,
  print '\ncost',
  for v in sorted(G): print D[v],
  print ''

def showFringe(G,F,D,inf):
  print '  fringe',
  for v in sorted(F):
    if D[v]!=inf:
      print v,D[v],' ',

G = {'A': [['B',4],['C',2]],
     'B': [['C',3],['D',2],['E',3]],
     'C': [['B',1],['D',4],['E',5]],
     'D': [],
     'E': [['D',1]]
}
G2 = {'A': [['B',8],['C',8],['D',9],['E',13],['F',4],['G',11]],
      'B': [['A',8],['C',0],['D',9],['E',12],['F',1],['G',18]],
      'C': [['A',8],['B',0],['D',3],['E', 7],['F',15],['G', 6]],
      'D': [['A',9],['B',9],['C',3],['E', 1],['F',13],['G', 9]],
      'E': [['A',13],['B',12],['C',7],['D',1],['F',18],['G', 6]],
      'F': [['A',4],['B',1],['C',15],['D',13],['F',18],['G', 5]],
      'G': [['A',11],['B',18],['C',6],['D',9],['F',6],['G', 5]]
}
G3 = {'A': [],
      'B': [['A',1]]
}
G4 = {'A': [['B',24],['F',4]],
      'B': [['A',24],['C',9],['G',23],['H',18]],
      'C': [['B',9],['D',7],['H',11]],
      'D': [['C',7],['E',21],['H',14]],
      'E': [['D',21],['F',16],['G',8],['H',10]],
      'F': [['A',4],['E',16],['G',6]],
      'G': [['B',23],['E',8],['F',6],['H',5]],
      'H': [['B',18],['C',11],['D',14],['E',10],['G',5]]
}
