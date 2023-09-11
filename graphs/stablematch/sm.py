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

n = 5
H = init_prefs(n)
R = init_prefs(n)
show_both(H,R)
