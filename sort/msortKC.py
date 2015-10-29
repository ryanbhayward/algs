import math
def k(n):
  L = [0,0]
  for j in range(2,n+1):
    L.append(j-1+ L[j/2] + L[(j+1)/2])
  return L[n]

def b(n):
  sum = 1.0
  for j in range(3,n+1):
    sum += math.log(j,2)
  return sum

def h(n):
  sum = 0.0
  for j in range(n,0,-1):
    sum += 1.0/(j*1.0)
  return sum

def c(n):
  return 2*(n+1)*h(n) - (17.0*n + 5.0)/6.0

for j in range(2,11):
  print j, k(j), b(j), c(j)
n = 10
for _ in range(6):
  n *= 10
  kk,bb = k(n), b(n)
  print n, kk,bb, c(n)
