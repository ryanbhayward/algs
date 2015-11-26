from math import sqrt, pi, exp
def choose(n, k):
# stackoverflow.com/questions/3025162/statistics-combinations-in-python
#    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    if 0 <= k <= n: 
      ntok, ktok = 1, 1
      for t in xrange(1, min(k, n - k) + 1):
        ntok *= n
        ktok *= t
        n -= 1
      return ntok // ktok
    else: return 0

def approx(n): #Stirling approx of n choose n/2
# use n! ~ sqrt(2 pi n) (n/e)^n 
  return pow(2,n) / sqrt(pi * n / 2.0)

def approx2(n): #better approx of n choose n/2, see wikipedia
# use n! ~ (usual approx) * e^(1/(12 n))
  return exp(-1.0/(4.0*n)) * approx(n)

for j in range(1,501):
  n, s = 2*j, "%12.10e"
  print n, s % choose(n,j), s % approx(n), s % approx2(n)
