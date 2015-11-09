import random  # longest increasing subsequence

def genseq(n):
  S = []
  for _ in range(n): S.append(random.randint(1,n))
  return S

def longest(S):
  L= [1] # L[j]: length longest subsequence ending at position j
  for k in range(1,len(S)):
    mymax = 0
    for j in range(k):
      if S[j]<S[k]: mymax = max(mymax,L[j])
    L.append(1+mymax)
  return L

#S = [7,10,6,2,4,8,9,3,2,7,9,1]
#S = [1,9,7,2,3,9,8,4,2,6,10,7]
S = [8,3,2,7,4,9,1,11,5]
#S = genseq(10); print S
print S
L = longest(S); print L
