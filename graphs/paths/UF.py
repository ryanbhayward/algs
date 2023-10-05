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
  print('myunion',x,y,'P')
  #rootx, rooty = myfind(x,P), myfind(y,P)
  rootx, rooty = findGP(x,P), findGP(y,P)
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

n = 10
P = [j for j in range(n)]
print(P)
for j in range(9):
  myunion(j,j+1,P)
  print(P)
