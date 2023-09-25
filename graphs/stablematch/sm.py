#stable matching demo          rbh 2023
#exhaustively find all stable matchings
#todo: add polytime propose/reject algm

from random import shuffle
from itertools import permutations

def pref_system_size(H,R):
  n = len(H)
  assert(n==len(R))
  return n

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
  n = pref_system_size(L,M)
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

def is_stable(A,B,m):
  n, minv, unhappy = len(m), inverse_perm(m), False
  for j in range(n):
    for k in range(n):
      if unhappy_couple(A,B,m,minv,j,k):
        return False
  return True

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

def propose_reject(H,R):
# C[j] is preferred-list index of best-so-far resident for hostpital j
# P[H[j][C[j]]] is best-so-far (not yet rejected by) resident for hospital j
# F[k] is best-so-far (among proposals) hospital for resident k

  n = pref_system_size(H,R)
  F = [None] * n
  C = [0 for j in range(n)]
  rejection = True
  while rejection:
    rejection = False
    for j in range(n):
      # make proposal
      h_choice = H[j][C[j]]
      if F[h_choice] == None:
        F[h_choice] = j
      elif F[h_choice] != j: # F has two proposals
        r_choice = F[h_choice] # F's current proposal
        if prefers(R[h_choice], j, r_choice):
          F[h_choice] = j
          j_reject = r_choice
        else:
          j_reject = j
        C[j_reject] += 1 # reject proposal from H[j_reject][C[j_reject]] 
        rejection = True     # one proposal will now be rejected
  P = [H[j][C[j]] for j in range(n)]
  print(P,C,F)
  return P

H = [[2,1,3,0], [0,3,1,2], [0,1,2,3], [3,0,2,1]]
R = [[3,2,0,1], [2,3,1,0], [2,0,1,3], [2,0,1,3]]
all_stable_matchings(H,R)

H = [[0,1],[1,0]]
for R in ([[0,1],[1,0]],
          [[0,1],[1,0]],
          [[1,0],[0,1]],
          [[1,0],[1,0]],
          [[0,1],[0,1]]):
  all_stable_matchings(H,R)

H = [[2,1,3,0], [0,3,1,2], [0,1,2,3], [3,0,2,1]]
R = [[3,2,0,1], [2,3,1,0], [2,0,1,3], [2,0,1,3]]
show_both(H,R)
m = propose_reject(H,R)
assert(is_stable(H,R,m))
m = propose_reject(R,H)
assert(is_stable(R,H,m))

H = [[2,1,3,0], [0,3,1,2], [1,0,2,3], [3,0,2,1]]
R = [[3,2,0,1], [1,3,0,2], [2,3,1,0], [2,0,1,3]]
show_both(H,R)
m = propose_reject(H,R)
assert(is_stable(H,R,m))
m = propose_reject(R,H)
assert(is_stable(R,H,m))
