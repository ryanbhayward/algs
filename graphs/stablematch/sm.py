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

def pref_system_size(H,R):
  n = len(H)
  assert(n==len(R))
  return n

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
# C[j]:       pref-list index           for hospital j
# H[j][C[j]]: current proposed resident for hospital j
# F[k]:       current maybe hospital    for resident k
  n = pref_system_size(H,R)
  F,C = [None] * n, [0 for j in range(n)]
  rejection, rounds = True, 0
  while rejection:
    rejection, rounds = False, rounds + 1
    print('     round', rounds)
    for j in range(n):
      h_choice = H[j][C[j]] # current H proposal
      if F[h_choice] == None: # R has no proposals
        F[h_choice] = j
        print(' ',j,' prop ',h_choice,': maybe',sep='')
      elif F[h_choice] != j: # R has two proposals
        r_maybe = F[h_choice] # R's current proposal
        if prefers(R[h_choice], j, r_maybe):
          r_reject, r_maybe = r_maybe, j
          F[h_choice] = r_maybe
        else:
          r_reject = j
        print(' ',j,' prop ',h_choice,
              ': pref ',r_maybe,', rej ', r_reject, sep='')
        C[r_reject] += 1 # H[j_reject] consider next pref
        rejection = True # a proposal was rejected
  P = [H[j][C[j]] for j in range(n)]
  print('\nj  P  C  F   ',rounds,'rounds')
  [print(j, P[j], C[j], F[j], sep='  ') for j in range(n)]
  return P

def propose_demo(H,R):
  show_both(H,R)
  print('\npropose_reject(H,R)')
  m = propose_reject(H,R)
  assert(is_stable(H,R,m))
  print('\npropose_reject(R,H)')
  m = propose_reject(R,H)
  assert(is_stable(R,H,m))

def mydemo():
#  H = [[0,1],[1,0]]
#  for R in ([[0,1],[1,0]],
#            [[1,0],[0,1]],
#            [[1,0],[1,0]],
#            [[0,1],[0,1]]):
#    all_stable_matchings(H,R)
#    propose_demo(H,R)

  H = [[2,1,3,0], [0,3,1,2], [0,1,2,3], [3,0,2,1]]
  R = [[3,2,0,1], [2,3,1,0], [2,0,1,3], [2,0,1,3]]
#  R = [[3,2,0,1], [1,3,0,2], [2,3,1,0], [2,0,1,3]]
  all_stable_matchings(H,R)
  propose_demo(H,R)
#  n = 8
#  H = random_prefs(n)
#  R = random_prefs(n)
#  propose_demo(H,R)

mydemo()
