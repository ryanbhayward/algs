def fwapsp(G):
  n = len(G)
  D = [[0 for x in xrange(n)] for y in xrange(n)]
  for x in range(n):
    for y in range(n):  D[x][y] = G[x][y]
  show(D)
  for t in range(n):
    print 't', t
    for x in range(n):
      for y in range(n):
        #D[x][y] = min(D[x][y], D[x][t] + D[t][y])
        dold, dnew = D[x][y], D[x][t] + D[t][y]
        if dnew < D[x][y]:
          D[x][y] = dnew
          print 'from',x,'to',y,'was',dold,'now', dnew
    show(D)

def show(D):
  for x in range(len(D)):
    for y in range(len(D)):
      print D[x][y],
    print ''
  print ''
G = [ [0, 9, 1, 5, 4],
      [9, 0, 7, 8, 2],
      [1, 7, 0, 6, 1],
      [5, 8, 6, 0, 1],
      [4, 2, 1, 1, 0] ]
fwapsp(G)
