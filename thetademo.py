from math import log
'''
an example of a function that is in Theta(n^{2.5}),
but the ratio of f(2n)/f(n), expected
to be about (2n)^{2.5} / n^{2.5} or roughly 5.6,
is about ten times that when n is 3700000...

why? because at this value of n, 
the slower growing log(n)^{90} dominates ...
once n gets large enough, the faster growing n^{2.5} dominates :)
'''

def f(n):
  return n**2.5

def g(n):
  return n**2.5 + (log(n))**90

for n0 in [3700000, 4000000000000000]:
  print(2*n0, n0, f(2*n0) / f(n0), g(2*n0) / g(n0))
