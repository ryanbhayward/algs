# used for weighted graphs
from sys import stdin
from re import findall
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

def readWGraph():
  G = {}
  for line in stdin:
    tokens =  findall(r"[^\W\d_]+|\d+", line)
    if len(tokens)>0:
      node = tokens.pop(0)
      nbrs = []
      while len(tokens)>0: 
        nbrs.append([tokens.pop(0), int(tokens.pop(0))])
    G[node] = nbrs
  return G

def showGraph(G):
  print '{'
  for node in sorted(G):
    print '\''+node+'\':',G[node],','
  print '}'

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
G5 = {'A': [['B', 18], ['D', 47], ['E', 15]] ,
      'B': [['C', 13], ['E', 30], ['F', 18]] ,
      'C': [['B', 9], ['F', 16], ['G', 21]] ,
      'D': [['E', 7], ['H', 20]] ,
      'E': [['F', 29], ['H', 7], ['I', 15]] ,
      'F': [['G', 8]] ,
      'G': [['J', 7]] ,
      'H': [['D', 12], ['I', 6]] ,
      'I': [['F', 11], ['J', 29]] ,
      'J': [['F', 5]]
}
G6 = {
'A': [['B', 24], ['D', 4], ['F', 14], ['H', 11]] ,
'B': [['A', 24], ['C', 9], ['E', 18]] ,
'C': [['B', 9], ['G', 7], ['J', 17]] ,
'D': [['A', 4], ['E', 21], ['F', 7]] ,
'E': [['B', 18], ['D', 21], ['G', 16], ['I', 10]] ,
'F': [['A', 14], ['D', 7], ['H', 7], ['K', 9]] ,
'G': [['C', 7], ['E', 16], ['J', 3], ['L', 15], ['M', 8]] ,
'H': [['A', 11], ['F', 7], ['K', 12], ['Q', 25]] ,
'I': [['E', 10], ['K', 19], ['L', 7]] ,
'J': [['C', 17], ['G', 3], ['M', 13], ['S', 19]] ,
'K': [['F', 9], ['H', 12], ['I', 19], ['O', 2]] ,
'L': [['G', 15], ['I', 7], ['M', 9], ['N', 12]] ,
'M': [['G', 8], ['J', 13], ['L', 9], ['P', 14]] ,
'N': [['L', 12], ['O', 17], ['R', 6]] ,
'O': [['K', 2], ['N', 17], ['Q', 8]] ,
'P': [['M', 14], ['S', 17], ['R', 13]] ,
'Q': [['H', 25], ['O', 8], ['R', 23]] ,
'R': [['N', 6], ['P', 13], ['Q', 23], ['S', 14]] ,
'S': [['J', 19], ['P', 17], ['R', 14]] ,
}
#Gtest = readWGraph()
#print Gtest
#showGraph(Gtest)
