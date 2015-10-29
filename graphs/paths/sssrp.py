def infinity(): return 999
def sssrp(G,source): #single source shortest reliable paths
  n,D = len(G), {}
  for v in G: D[v] = infinity()
  D[source] = 0
  show(D)
  for t in range(n):
    print 'source',source,' at most', t+1, 'edges'
    newD = {}
    for v in G: newD[v] = D[v]
    for v in G:
      for wd in G[v]:
        if wd[0]!=source:
          dfromv = D[v] + wd[1]
          if dfromv < newD[wd[0]]:  
            newD[wd[0]] = dfromv
            print '   ',wd[0],'via',v,'now',dfromv
    for v in G: D[v] = newD[v]
    show(D)
def show(D):
  #for v in sorted(G): print '%4s' % v,
  #print ''
  for v in sorted(G): print '%4d' % D[v],
  print ''

#G = {'A': [['B',8],['C',8],['D',9],['E',13],['F',4],['G',11]],
     #'B': [['A',8],['C',0],['D',9],['E',12],['F',1],['G',18]],
     #'C': [['A',8],['B',0],['D',3],['E', 7],['F',15],['G', 6]],
     #'D': [['A',9],['B',9],['C',3],['E', 1],['F',13],['G', 9]],
     #'E': [['A',13],['B',12],['C',7],['D',1],['F',18],['G', 6]],
     #'F': [['A',4],['B',1],['C',15],['D',13],['F',18],['G', 5]],
     #'G': [['A',11],['B',18],['C',6],['D',9],['F',6],['G', 5]]}
G = {'S': [['A',1],['C',2]],
     'A': [['S',1],['B',2],['D',5]],
     'B': [['A',2],['D',1],['T',4]],
     'C': [['S',2],['D',3]],
     'D': [['A',5],['B',1],['C',3],['T',1]],
     'T': [['B',4],['D',1]]}
sssrp(G,'S')
