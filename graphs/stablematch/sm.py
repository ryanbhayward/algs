#stable matching demo rbh 2023
from random import shuffle

def init_prefs(n):
  pref = list(range(n))
  L = []
  for _ in range(n):
    shuffle(pref)
    L.append(pref.copy())
  return L

def show_prefs(L):
  for j in range(len(L)):
    print(j, L[j])

def show_both(L,M):
  n = len(L)
  assert(n==len(M))
  for j in range(n):
    print(j, L[j], M[j])

def prefers(L,x,y): # in L, is x preferred to y?
  return (L.index(x) < L.index(y))

def unstable_pair(A,B,e,f):# prefs, prefs, edge, edge
  if (prefers(A[e[0]],f[1],e[1]) and prefers(B[e[1]],f[0],e[0])) or \
     (prefers(A[f[0]],e[1],f[1]) and prefers(B[f[1]],e[0],f[0])):
    print('unstable pair', e, f)
    return True
  return False

def is_stable(A,B): # is (A,B) stable?
  n = len(A)
  for j in range(n-1):
    for k in range(j+1,n):
      if unstable_pair(A,B,(j,j),(k,k)):
        return False
  return True

n = 3
H = init_prefs(n)
R = init_prefs(n)
show_both(H,R)
x = is_stable(H,R)
