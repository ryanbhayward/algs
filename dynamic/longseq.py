import random  # longest increasing subsequence

def genseq(n):
  S = []
  for _ in range(n): S.append(random.randint(1,n))
  return S

def longest(S):
  L= [1]
  for k in range(1,len(S)):
    mymax = 0
    for j in range(k):
      if S[j]>S[k]: mymax = max(mymax,L[j])
    L.append(1+mymax)
  return L

def long(S):
  n = len(S); print S
  if n==1: return 1
  mymax = 1
  for j in range(1,len(S)):
    for i in range(j):
      print i,j
      if S[i]<S[j]: mymax = max(mymax,1+long(S[:i+1]))
  return mymax

def X(n):
  print 'X(',n,')'
  if n==1: 
    return 1
  mymax = 1
  for j in range(n-1):
    mymax = max(mymax,X(j+1))
  return 1 + mymax

def Y(n):
  print 'Y(',n,')'
  if n>0:
    for j in range(n): #from 0 to n-1
      Y(j)

S = [7,10,6,2,4,8,9,3,2,7,9,1]
#S = genseq(10); print S
L = longest(S); print L
