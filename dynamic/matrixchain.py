import random  # matrix chain multiplication 

def genseq(n):
  S = []
  for _ in range(n): S.append(2+random.randint(1,n))
  return S

def mincost(M): #matrix dimensions
  n = len(M)-1
  C = [[0 for x in xrange(n)] for x in xrange(n)]
  for j in range(n-1):
    C[j][j+1] = M[j]*M[j+1]*M[j+2]
  for span in range(2,n):
    for i in range(n-span):
      vals = []
      j = i+span
      for t in range(i,i+span):
        z = C[i][t]+C[t+1][j]+M[i]*M[t+1]*M[j+1]
        #print i,t,j,z
        vals.append(z)
      C[i][j] = min(vals)
      del vals[:]
  return C

S = [5, 3, 7, 1, 6]
C = mincost(S); print C
#S = genseq(9); print S
#C = mincost(S); print C
