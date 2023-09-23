#stable matching demo          rbh 2023
#exhaustively find all stable matchings
#todo: add polytime propose/reject algm

from random import shuffle
from itertools import permutations

def random_prefs(n):
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
  print('    preference lists')
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
    return True
  return False

def all_unhappy(A,B,m): # prefs, prefs, matching m:A -> B
  U = []
  n, minv, unhappy = len(m), inverse_perm(m), False
  for j in range(n):
    for k in range(n):
      if unhappy_couple(A,B,m,minv,j,k):
        U.append((j,k))
  return U

def all_stable_matchings(H,R):
  show_both(H,R)
  for m in list(permutations(range(len(H)))):
    minv = inverse_perm(m)
    U = all_unhappy(H,R,m)
    print(m, end=' ')
    if len(U)==0:
      print('stable')
    else:
      print('unhappy', end='')
      [print(u, end='') for u in U]
      print('')
  print('')

H = [[2,1,3,0], [0,3,1,2], [0,1,2,3], [3,0,2,1]]
R = [[3,2,0,1], [2,3,1,0], [2,0,1,3], [2,0,1,3]]
all_stable_matchings(H,R)

H, R = [[0,1],[1,0]], [[1,0],[0,1]]
all_stable_matchings(H,R)

H, R = [[0,1],[1,0]], [[0,1],[1,0]]
all_stable_matchings(H,R)

H, R = [[0,1],[0,1]], [[0,1],[1,0]]
all_stable_matchings(H,R)

H, R = [[0,1],[0,1]], [[1,0],[0,1]]
all_stable_matchings(H,R)

H, R = [[0,1],[0,1]], [[1,0],[1,0]]
all_stable_matchings(H,R)

H, R = [[0,1],[0,1]], [[0,1],[0,1]]
all_stable_matchings(H,R)
