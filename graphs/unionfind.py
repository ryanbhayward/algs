def myfind(x, parents):
  px = parents[x]
  if x==px: return x
  gx = parents[px]
  while px != gx:
    parents[x] = gx
    x = px ; px = gx ; gx = parents[gx]
  return px

def myunion(x,y,parents): 
  rx = myfind(x,parents)
  ry = myfind(y,parents)
  parents[rx] = ry

n = 16
P = []
for j in range(n):
  P.append(j)

print P
t = 2
while t <= n:
  print t
  for j in range(n/t):
    myunion(t*j, t*j+t/2,P) ; print P
  t *= 2
