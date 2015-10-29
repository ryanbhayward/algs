import time

def fib(n):
  if (n<=1):
    return n
  return fib(n-1) + fib(n-2)

t1 = 1.0
for n in range(100):
  now, fn = time.time(), fib(n)
  t0, t1  = t1, time.time()-now
  print n, fn, t1, "sec, ratio current/prev", t1/t0
