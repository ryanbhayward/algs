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

def showfa(f, a):
  if not f:
    print(a)
  else:
    print('unsatisfiable, last a:', a)

def sat(f):
  return not f #  True iff  f is empty list

def unsat(a):
  return not a # True iff a is empty string

def fix_literal(t, f, a): # in f, set literal t True, return updated a
  print('fix', t, end=' ')
  index = abs(t)-1
  if a[index] == (FALSE if (t>0) else TRUE): # contradiction, f unsatisfiable
    print('   xxxxxx')
    return ''
  a = a[:index] + (TRUE if (t>0) else FALSE) + a[index+1:]
  for c in f:
    if t in c:
      f.remove(c)
    elif -t in c:
      c.remove(-t)
      if len(c)==0:     # clause empty so f unsatisfiable
        print('   y y y y')
        return ''
  return a

def fix_and_propagate(t, f, a):  # set literal t and propagate
  a = fix_literal(t, f, a)
  if unsat(a) or sat(f):
    return a
  t = f.index(min(f,key=len))  # clause with fewest literals
  assert(len(f) > 0)
  if len(f[t])==1:
    return fix_and_propagate(f[t][0], f, a)
  return a

n, k, m = 5, 2, 12
myf = formula(n, k, m)

#myf = [
#[1, 2],
#[1, -2],
#[-1, 3],
#[-1, 5],
#[-1, -5],
#[2, -5],
#[3, -4]
#]

print('formula with', n, 'vars', m, 'clauses')
showf(myf)

for j in range(1, n+1):
  for t in [j, -j]:
    a, f = UNKNOWN*m, deepcopy(myf)
    print('\nstart', t, '  ', a)
    showf(f)
    a = fix_and_propagate(t, f, a)
    print('\nfinished, a =', a)
    showf(f)
    
