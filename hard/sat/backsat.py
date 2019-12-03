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

def fix_literal(t, f, a): # in f, set literal t True, return updated a
  #print('fix_literal',t)
  index = abs(t)-1
  if a[index] != UNKNOWN:
    print('t', t, 'index', index)
    showfa(f, a)
    assert False
  a = a[:index] + (TRUE if (t>0) else FALSE) + a[index+1:]
  newf = [c for c in f if t not in c]
  for c in newf:
    if -t in c:
      c.remove(-t)
      if len(c)==0:
        return [], ''
  #print(newf)
  return newf, a

def fix_and_propagate(t, f, a):  # set literal t and propagate
  #print('fl', f, t, a)
  f, a = fix_literal(t, f, a)
  if unsat(a) or sat(f): 
    return [], a
  t = f.index(min(f,key=len))  # clause with fewest literals
  if len(f[t])==0:  # unsat
    return [], ''
  if len(f[t])==1: 
    return fix_and_propagate(f[t][0], f, a)
  return f, a

def mycopy(f, a):
  newf = []
  for clause in f: 
    newf.append(list(clause))
  return newf, a

def sat(f): 
  return not f #  True iff  f is empty list

def unsat(a): 
  return not a # True iff a is empty string

def ind_short(f):
  return f.index(min(f, key=len)) # index of clause with fewest literals

def backsat(f, a):
  if unsat(a) or sat(f):
    return f, a
  while True:
    ndx = ind_short(f)
    lenj = len(f[ndx])
    if lenj==0:
      return f, ''
    elif lenj==1: 
      f, a = fix_and_propagate(f[ndx][0], f, a)
    else:
      break
  #split: 2 possible bool. vals for literal f[ndx][0]
  fcopy, acopy = mycopy(f, a)
  ndx = ind_short(f)
  f, a = fix_and_propagate(f[ind_short(f)][0], f, a) 
  if not unsat(a) and sat(f): 
    print('happ')
    return f, a
  f, a = backsat(f, a)
  if not unsat(a) and sat(f): 
    print('happ')
    return f, a
  f, a = fcopy, acopy
  ndx = ind_short(f)
  f, a = fix_and_propagate(-f[ndx][0], f, a)
  return backsat(f, a)

def backsolve(n,myf):
  asn = UNKNOWN * n
  assert(not sat(myf))
  return backsat(myf,asn)

#n,myf=6,[[-5,-6],[-3,5],[-2,5],[1,-6],[1,-4],[1,-3],[2,3],[2,6],[3,-5],[3,4],[4,-5],[5,-6]]
#n,myf=6,[[-4,-5,6],[-4,5,-6],[-2,4,-5],[-2,5,-6],[-1,-3,-4],[-1,-3,4],[-1,4,-6],[1,-4,5],[1,-3,-5],[1,-3,4],[1,5,-6],[2,5,6],[3,-5,-6],[4,-5,6],[4,5,-6],[4,5,6]]

#max m: (n choose k)(2^k)
#n, k, m = 20, 5, 400  # good example
#n, k, m = 30, 5, 100 # backtrack yes, bf too slow
n, k, m = 10, 3, 48  # good example

#n,myf = 5, [[1,-5],[-2,-3],[3,4],[-4,-5],[2,5],[-1,-5]]
#n,myf = 5, [[1,-2],[1,3],[-2,-3],[2,4],[-3,-4],[3,-5],[3,5]]

myf=[
[1, 2, 8], [1, 3, 4], [1, 6, -8], [1, 7, 8], [-1, 2, -5], [-1, 2, 9], [-1, -2, 8],
[-1, -2, 10], [-1, 3, 6], [-1, 4, 6], [-1, -4, 7], [-1, -6, 9], [2, -4, 7],
[2, 7, -8], [2, -7, -10], [2, -8, 10], [2, 9, -10], [-2, 3, -9], [-2, -3, 5],
[-2, -3, 7], [-2, 4, -8], [-2, 4, -9], [-2, -4, 5], [-2, -4, 10], [-2, 5, -9],
[-2, -5, 9], [-2, 6, -10], [-2, 7, 10], [-2, 8, 10], [3, -5, -9], [3, -8, -10],
[-3, 5, 9], [-3, 5, 10], [-3, 6, -10], [-3, -6, 10], [-3, -7, 8], [4, -5, 9],
[4, -5, -9], [4, 7, -10], [4, -7, -9], [5, -8, -10], [5, 9, 10], [-5, 6, 10],
[-5, 6, -10], [-5, -9, -10], [6, -7, 9], [6, 8, -10], [6, -8, -9]]
#n, k, m = 5, 3, 15  # good example
myf = formula(n,k,m)

myf2 = deepcopy(myf)
print('formula with', n, 'vars', m, 'clauses')
showf(myf)
print('')
print(backsolve(n, myf)[1])

print('\nverify with bfsolve')
bfsolve(n, myf2, True)
