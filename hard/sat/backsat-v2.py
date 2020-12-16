""" 
simple backtracking sat solver   revised RBH 2020
  * fixed bug found by Nectarios Chroniaris, thank you
  * this revision assisted by Fatima Davelouis Gallardo, thank you
version 2.0
  * added verbose feature, so you can see what's happenin' :)

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

def literal_index(t): return abs(t) - 1

def sat(f): return not f #  True iff f empty list

def unsat(a): return not a # True iff a empty string

def resolved(f, a): return not f or not a # f empty? sat, a empty? unsat

def fix_literal(t, f, a, verbose): # t -> T, return updated f, a
  if verbose: print(t, end=' ')
  index = literal_index(t)
  if a[index] == (FALSE if (t>0) else TRUE): # contradiction, f unsat
    if verbose: print('  *- contradiction -*')
    return f, ''
  a = a[:index] + (TRUE if (t>0) else FALSE) + a[index+1:]
  newf = []
  for c in f:
    if t not in c:
      newc = deepcopy(c)
      if -t in c:
        newc.remove(-t)
      if len(newc)==0:  # empty clause, so f unsat
        if verbose: print('  *- empty clause -*')
        return f, ''
      newf.append(newc)
  if verbose: print(newf)
  return newf, a

def ind_short(f): return f.index(min(f, key=len)) # ndx: clause, fewest literals

def backsat(f, a, v): # iter. backtrack: formula, assignment, verbose
  candidates = []  # list of partial solutions
  itns = 0
  while True:
    if v: print(len(candidates), 'candidates remain')
    itns += 1
    if v: print('\nitn',itns)
    if sat(f): 
      print('found solution ', a, '\niterations', itns)
      return f, a
    if unsat(a): 
      if len(candidates) > 0: 
        f, a = candidates.pop()
        if v: print('unsat pop ', end='')
        if v: print(f)
      else: 
        print('formula unsat, iterations', itns)
        return f, a, itns # 
    else: # f != empty list, a != empty string
      ndx = ind_short(f)
      lenj = len(f[ndx])
      if lenj == 1: # fix literal
        f, a = fix_literal(f[ndx][0], f, a, v)
      elif lenj >= 2: #try both possible values
        fcopy, acopy = deepcopy(f), a
        f, a        = fix_literal(f[ndx][0], f, a, v)  # try now
        if v: print('push')
        newf, newa  = fix_literal(-fcopy[ndx][0], fcopy, acopy, v)
        candidates.append((newf, newa))              # try later
      
def backsolve(n, myf, verbose):
  asn = UNKNOWN * n
  backsat(myf, asn, verbose)

n, k, m = 22, 3, 100
f = formula(n, k, m)
#f = [[1, 2, 3], [1, 2, -3], [1, 2, -4], [1, -2, 3], [1, -2, -4], [1, 3, 4], [1, 3, -4], [-1, 2, -3], [-1, 2, -4], [-1, -2, -3], [-1, -2, 4], [-1, -2, -4], [-1, 3, 4], [2, -3, -4], [-2, 3, 4], [-2, -3, -4]]
f2 = deepcopy(f)
print('formula with', n, 'vars', m, 'clauses')
print('')
verbose = True
backsolve(n, f, verbose)

#print('\nverify with bfsolve')
#bfsolve(n, f2, True)
