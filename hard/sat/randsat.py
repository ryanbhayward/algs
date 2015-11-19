#generate random t-uniform formula
from random import randint
# literals  x1 -x1 x2 -x2 ... output as 1 -1 2 -2 ...
# for sorting clauses,
#   literals 1 -1 2 -2 ...  n  -n   represented by 
#   integers 0  1 2  3 ... n-2 n-1
def litToInt(lit):
  if lit>0: return 2*lit-2
  return 2*(-lit)-1
def intToLit(n):
  if 0==n%2: return 1+n/2
  return          -(1+n/2)

def randclause(n,k): # n-var uniform random k-clause
# floyd's alg, from Bentley's prog. pearls "A sample of brilliance"
# if lit in clause then -lit not in clause
  S = []
  for j in range(n+1-k,n+1):
    t = randint(1,j)
    if S.count(t)>0: S.append(j)
    else:            S.append(t)
  S.sort()
  for j in range(k):
    if randint(0,1)==0: S[j] *= -1
  return S

def formula(n,t,m): # n variables, t-uniform, m clauses
  f = []
  while len(f)<m:
    new = randclause(n,t)
    duplicate = False
    for j in f:
      if new == j: duplicate = True
    if not duplicate:  f.append(new)
  # sort lexicographic using x1 < -x1 < x2 < -x2 < ...
  for m in range(len(f)):
    for c in range(len(f[m])): f[m][c] = litToInt(f[m][c])
  f.sort()
  for m in range(len(f)):
    for c in range(len(f[m])): f[m][c] = intToLit(f[m][c])
  return f

def prettyClause(c):
  psn = -1
  for lit in c:
    psn, psnOld = litToInt(lit), psn
    for j in range(psn-(psnOld+1)):  print '  ',
    print '%2d' % lit,
  print ''

def plainClause(c):
  print '[',  
  for j in range(len(c)-1): print '%2d,' % c[j],
  print '%2d]' % c[len(c)-1]
   
def show(f,pretty):
  for c in f:
    if pretty: prettyClause(c)
    else:       plainClause(c)

#f = formula(6,3,25)
#show(f,False)
#show(f,True)
