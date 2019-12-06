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

"""
warning: changes formula f
"""

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
  if resolved(f, a):
    return a
  t = f.index(min(f,key=len))  # clause with fewest literals
  #assert(len(f) > 0)
  if len(f[t])==1:
    return fix_and_propagate(f[t][0], f, a)
  return a

def mycopy(f, a):
  newf = []
  for clause in f: 
    newf.append(list(clause))
  return newf, a

def ind_short(f):
  return f.index(min(f, key=len)) # index of clause with fewest literals

def backsat(f, a):
  if resolved(f, a):
    return a
  while True:
    ndx = ind_short(f)
    lenj = len(f[ndx])
    if lenj==0:
      return ''
    elif lenj==1: 
      a = fix_and_propagate(f[ndx][0], f, a)
    else:
      break
  #split: 2 possible bool. vals for literal f[ndx][0]
  fcopy, acopy = mycopy(f, a)
  ndx = ind_short(f)
  a = fix_and_propagate(f[ind_short(f)][0], f, a) 
  a = backsat(f, a)
  if a:
    return a
  # f was unsatisfiable, try fcopy
  f, a = fcopy, acopy
  ndx = ind_short(f)
  a = fix_and_propagate(-f[ndx][0], f, a)
  return backsat(f, a)

def backsolve(n, myf):
  asn = UNKNOWN * n
  return backsat(myf,asn)

n, k, m = 25, 3, 105
myf = formula(n, k, m)

myf2 = deepcopy(myf)
print('formula with', n, 'vars', m, 'clauses')
showf(myf)
print('')
print(backsolve(n, myf))

#print('\nverify with bfsolve')
#bfsolve(n, myf2, False)
