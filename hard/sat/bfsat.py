from itertools import product
from randsat import show, formula
# solve with brute force sat solver
# I/O: literals x1 -x1 x2 -x2 ... rept'd by 1 -1 2 -2 ...

def clause_sat(clause,asnmt):
  for var in clause:
    if ((var>0 and asnmt[  var-1 ] == 1) or 
        (var<0 and asnmt[-(var+1)] == 0)): 
      return True
  return False

def sat(formula, asnmt):
  for clause in formula:
    if not clause_sat(clause,asnmt): return False
  return True

def bfsolve(n, myf, findAll): #try all assignments
  for a in product([0,1],repeat=n):
    if sat(myf,a): 
      for v in a: 
        print(v, end='')
      print('')
      if not findAll: return

  #below: fixed examples
n,myf=4, [
    [-1,2,3],
    [2,3,-4],
    [1,3,4],
    [-1,-2,-4],
    [1,-2,-3],
    #[1,-2,3],
    [1,2,-3],
    [-1,-2,4],
    [-1,2,-3]
    ]
#n,myf=4,[[-1,2,-4],[-1,-2,4],[-1,-3,-4],[-1,3,4],[-1,3,-4],[1,-2,4],[1,-2,-4],[1,3,4],[2,3,-4],[-1,2,-3]]
  #n, myf = 4, [[1,-2,3],[1,-2,-4],[1,2,3],[1,2,4],[-1,-2,-3],[-1,-2,3],[-1,2,4],[2,-3,-4],[2,3,-4]]
  #n, myf = 6, [[-4,-5,6],[-4,5,-6],[-2,4,-5],[-2,5,-6],[-1,-3,-4],[-1,-3,4],[-1,4,-6],[1,-4,5],[1,-3,-5],[1,-3,4],[1,5,-6],[2,5,6],[3,-5,-6],[4,-5,6],[4,5,-6],[4,5,6]]
  #m = len(myf)

#n, k, m = 25, 5, 360  #max m: (n choose k)(2^k)
#myf = formula(n,k,m)
show(myf, False)
bfsolve(n,myf,True)
