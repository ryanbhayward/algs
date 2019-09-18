import random  # longest increasing subsequence

def pretty(S): # print vector, uniform field width
  print "[",
  for j in S:
    print '%2d' % j, 
  print "]",

def genseq(n):
  S = []
  #for _ in range(n): S.append(random.randint(1,n))
  #return S
  for j in range(n): 
    S.append(j)
  random.shuffle(S)
  return S

def mmx(S):
  mx = S[0]
  for j in range(1,len(S)):
    if mx < S[j]: 
      mx = S[j]
  return mx

for j in range(1,10):
  S = genseq(j); pretty(S); print mmx(S), ""
