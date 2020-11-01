""" 
simple backtracking sat solver   revised RBH 2019

literals  x_1 ...  x_n represented by  1  2 ...  n
literals -x_1 ... -x_n represented by -1 -2 ... -n
partial assignment vector  
  *  length n string    e.g. ?0?11??1
  *  length 0 if unsatisfiable
"""

from randsat import formula
from bfsat import bfsolve
from copy import deepcopy
UNKNOWN, FALSE, TRUE = '?', '0', '1'

def showf(f): 
  print('formula now has length', len(f))
  for j in f: 
    print(j)

def literal_index(t):
  return abs(t) - 1

def sat(f):
  return not f #  True iff  f is empty list

def unsat(a):
  return not a # True iff a is empty string

def resolved(f, a): # satisfied if f empty, unsatisfied if a empty
  return not f or not a

def fix_literal(t, f, a): # set literal t True, return updated f, a
  print('fix', t, end=' ')

  index = literal_index(t)
  if a[index] == (FALSE if (t>0) else TRUE): # contradiction, f unsatisfiable
    print('  *- contradiction -*')
    return f, ''
  a = a[:index] + (TRUE if (t>0) else FALSE) + a[index+1:]
  newf = []
  for c in f:
    if t not in c:
      if -t in c:
        c.remove(-t)
      if len(c)==0:     # empty clause so f unsatisfiable
        print('  *- empty clause -*')
        return f, ''
      newf.append(list(c))
  showf(newf)
  print(a)
  return newf, a

def ind_short(f):
  return f.index(min(f, key=len)) # index of clause with fewest literals

def backsat(f, a): # simple iterative backtracking sat solver
  print('backsat', f, a)
  candidates = []  # list of partial solutions
  while True:
    print(len(candidates), 'other candidates')
    if sat(f): # f empty list
      print('found solution ', a)
      return f,a
    if unsat(a):  # a empty string
      if len(candidates) > 0:
        f, a = candidates.pop()
      else: 
        print('formula unsatisfiable')
        return f,a # 
    else: # f is not the empty list, a is not the empty string
      ndx = ind_short(f)
      lenj = len(f[ndx])
      if lenj == 1: # fix literal
        f, a = fix_literal(f[ndx][0], f, a)
      elif lenj >= 2: #try both possible values
        fcopy, acopy = deepcopy(f), a
        f, a        = fix_literal( f[ndx][0], f, a)
        newf, newa  = fix_literal(-f[ndx][0], fcopy, acopy)
        candidates.append((newf, newa))
      
def backsolve(n, myf):
  asn = UNKNOWN * n
  backsat(myf, asn)

n, k, m = 4, 3, 16
f = formula(n, k, m)
f = [[1, 2, 3], [1, 2, -3], [1, 2, -4], [1, -2, 3], [1, -2, -4], [1, 3, 4], [1, 3, -4], [-1, 2, -3], [-1, 2, -4], [-1, -2, -3], [-1, -2, 4], [-1, -2, -4], [-1, 3, 4], [2, -3, -4], [-2, 3, 4], [-2, -3, -4]]
f2 = deepcopy(f)
print('formula with', n, 'vars', m, 'clauses')
print('')
backsolve(n, f)

print('\nverify with bfsolve')
bfsolve(n, f2, True)
