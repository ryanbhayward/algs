# use simple find,      simple union, or
#     gp compress find, simple union, or
#     simple find,      union by rank 

def myfind(v,P): # simple find
  while P[v] != v:
    v = P[v]
  return v

def findGP(x, parents): # find, gp compress
  px = parents[x]
  if x==px: return x
  gx = parents[px] # grandparent
  while px != gx:
    parents[x] = gx
    x = px ; px = gx ; gx = parents[gx]
  return px

def myunion(x,y,P): # simple union
  rootx, rooty = myfind(x,P), myfind(y,P)
  P[rootx] = rooty

def unionBR(v,w,P,R): # union by rank
  rv,rw = myfind(v),myfind(w)
  if   R[rv] < R[rw]: 
    P[rv] = rw
  elif R[rv] > R[rw]: 
    P[rw] = rv
  else:
    P[rv] = rw
    R[rw] += 1

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
