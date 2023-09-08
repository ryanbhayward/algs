# I can't remember what this is!
# maybe computing square roots base 4?

def basefour(n):
  L = []
  while n > 0: 
    L.append(n % 4)
    n = n / 4
  return L

def sqrt(n): 
  q,r = 0,0   # quotient remainder
  L = basefour(n)
  print L
  for j in reversed(L): 
    q, v, r = 2*q, 4*q, 4*r + j #v: divisor
    if v+1 <= r: # set digit to 1
      q,r = q+1, r - (v+1)
  return q,r

def test(n):
  for j in range(1,n):
    assert sqrt(j*j) == (j,0)
    assert sqrt(j*j+j-1) == (j,j-1)
  print 'passed', n

print 62, sqrt(62)
test(100)
