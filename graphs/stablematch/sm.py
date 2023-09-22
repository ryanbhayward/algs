#stable matching demo rbh 2023
#todo: add propose/accept rounds
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
  print('both preference lists')
  for j in range(n):
    print(j, ' ', L[j], ' ', M[j])

def prefers(L,x,y): # in L, is x preferred to y?
  return (L.index(x) < L.index(y))

def inverse_perm(P):
  I, n = [], len(P)
  for j in range(n):
    I.append(P.index(j))
  for j in range(n):
    assert(I[P[j]]==j)
  return I

def unhappy_couple(A,B,m,minv,x,y):
  if y == m[x]: return False
  mx, my = m[x], minv[y] # mates of x and y
  if (prefers(A[x],y,mx) and prefers(B[y],x,my)):
    print(x,y,',',end=' ')
    return True
  return False

def is_stable(A,B,m): # prefs, prefs, matching m:A -> B
  n, minv, unhappy = len(m), inverse_perm(m), False
  print('unhappy couples:', end = ' ')
  for j in range(n):
    for k in range(n):
      if unhappy_couple(A,B,m,minv,j,k):
        unhappy = True
  print('')
  return not unhappy

n = 2
H, R = init_prefs(n), init_prefs(n)
show_both(H,R)
m = list(range(n))

n = 4
H = [[2,1,3,0], [0,3,1,2], [0,1,2,3], [3,0,2,1]]
R = [[3,2,0,1], [2,3,1,0], [2,0,1,3], [2,0,1,3]]
m = [3,0,2,1]
m = [2,1,0,3]
m = [2,3,1,0]
m = [2,3,0,1]

minv = inverse_perm(m)
print('matching and inverse', m, minv)
if is_stable(H,R,m):
  print('stable')
else:
  print('unstable')
