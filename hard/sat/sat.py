from itertools import product
from randsat import show, formula
# solve with brute force sat solver
# I/O: literals x1 -x1 x2 -x2 ... rept'd by 1 -1 2 -2 ...

def clausesat(clause,asnmt):
  for var in clause:
    if ((var>0 and asnmt[var-1]==1) or 
       (var<0 and asnmt[-(var+1)]==0)): 
      return True
  return False

def sat(formula, asnmt):
  for clause in formula:
    if not clausesat(clause,asnmt): return False
  return True

def emptyAsnmt(n):
  a = [UNKNOWN]*n
  return a
  
#n,m = 4,9  #max m is n choose k times 2^k, where k=2or3
#myf = formula(n,3,m)
#myf = [[-1,2], [-2,3], [-3,4], [1,2], [-2,-4]]
#myf = [[-1,2], [-2,3], [-2,-3], [1,2]]
#print "\nrandom formula",n,"vars",m,"clauses"

myf = [
[  1, -2,  3],
[  1, -2, -4],
[  1,  2,  3],
[  1,  2,  4],
[ -1, -2, -3],
[ -1, -2,  3],
[ -1,  2,  4],
[  2, -3, -4],
[  2,  3, -4]
]
myf = [
[-4, -5, 6],
[-4, 5, -6],
[-2, 4, -5],
[-2, 5, -6],
[-1, -3, -4],
[-1, -3, 4],
[-1, 4, -6],
[1, -4, 5],
[1, -3, -5],
[1, -3, 4],
[1, 5, -6],
[2, 5, 6],
[3, -5, -6],
[4, -5, 6],
[4, 5, -6],
[4, 5, 6]
]
#n,m = 6, len(myf)

n, m = 20, 90
myf = formula(n,3,m)
allAsn = product([0,1],repeat=n)

show(myf, False)
show(myf, True)

done = False
for a in allAsn:
  if sat(myf,a): 
    print 'satisfiable', a
    done = True
    exit
if not done: print 'unsatifsiable'
