# simple implementation of old-school square root algorithm RBH2023
#   (my parent showed me this, not sure what it is called)
# input: positive integer n
# output: q = floor(sqrt(n)), and remainder r = q*q

def basehundred(n):
  L = []
  while n > 0: 
    L.append(n % 100)
    n = n // 100
  L.reverse()
  return L

def ossqrt(n): 
  q, r = 0,0   # quotient, remainder
  L = basehundred(n)
  for dd in L: #dd  next digit-pair from n
    s = 20*q   #LHS multiplier
    q, r = 10*q, 100*r + dd
    digit = 0
    while ((s+digit+1)*(digit+1) <= r):
      digit += 1
    assert((0 <= digit) and (digit <= 9))
    q, r = q + digit, r - (s+digit)*digit
  assert(q*q <= n and ((q+1)*(q+1)) > n)
  return q, r

n = 1234981234120109871234
print(n, ossqrt(n))
