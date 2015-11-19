from randsat import formula
# generate random uniform 2- or 3-sat formula
# solve with simple backtracking

# literals  x_1 ...  x_n represented by  1  2 ...  n
# literals -x_1 ... -x_n represented by -1 -2 ... -n

# assignment vector: one entry for each variable
# set a[0] to UNSAT if formula unsatisfiable
UNSAT, UNKNOWN, FALSE, TRUE = -2, -1, 0, 1

def showf(f): 
  for j in f: print j

def showfa(f,a):
  for x in a: 
    if x==UNSAT: print '*',
    elif x==UNKNOWN: print '?',
    else: print x,
  print ''
  showf(f)

def fixliteral(t, f, a): # in f, set literal t True, update a
  index = abs(t)-1
  #print "set var",index+1, ("T" if t>0 else "F")
  assert a[index]== UNKNOWN
  a[index] = (TRUE if t>0 else FALSE)
  for clause in f[:]:
    clauseSat = False
    for literal in clause[:]:
      if literal == -t:
        clause.remove(literal)
        if len(clause)==0: # f unsat
          a[0] == UNSAT
          return
      elif literal == t: 
        clauseSat = True
    if clauseSat: f.remove(clause)

def mycopy(f,a):
  newa = list(a)
  newf = []
  for clause in f: newf.append(list(clause))
  return newf, newa

def sat(f): return (True if len(f)==0 else False)
def unsat(a): return (True if a[0]==UNSAT else False)

def backsat(f,a):
  if unsat(a) or sat(f): return f,a
  minj = f.index(min(f,key=len))  # clause with fewest literals
  if len(f[minj])==0:
    a[0] = UNSAT
    return f,a
  if len(f[minj])==1: 
    fixliteral(f[minj][0], f, a)
    return backsat(f,a)
  #split: 2 possible bool. vals for literal f[minj][0]
  #print "split A:", f[minj][0]
  fcopy, acopy = mycopy(f,a)
  fixliteral(f[minj][0], f, a)  # f[minj][0] True
  f,a = backsat(f,a)
  if sat(f): return f, a
  f,a = fcopy, acopy
  #print "split B:", -f[minj][0]
  fixliteral(-f[minj][0], f, a) # f[minj][0] False
  return backsat(f, a)

#myf=[[-5,-6],[-3,5],[-2,5],[1,-6],[1,-4],[1,-3],[2,3],[2,6],[3,-5],[3,4],[4,-5],[5,-6]]
#myf=[[-4,-5,6],[-4,5,-6],[-2,4,-5],[-2,5,-6],[-1,-3,-4],[-1,-3,4],[-1,4,-6],[1,-4,5],[1,-3,-5],[1,-3,4],[1,5,-6],[2,5,6],[3,-5,-6],[4,-5,6],[4,5,-6],[4,5,6]]

n,m = 20,90  #max m is n choose k times 2^k, where k=2or3
myf = formula(n,3,m)
print "\nrandom formula",n,"vars",m,"clauses"
showf(myf)
print ''
asn = [UNKNOWN]*n
f,a = backsat(myf,asn)
showfa(f,a)
