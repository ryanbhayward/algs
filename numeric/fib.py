
import time
# three versions of fibonacci function

def fib(n):  # recursive 
  if (n<=1):
    return n
  return fib(n-1) + fib(n-2)

def ifib(n): # iterative 
  a,b = 0,1
  for _ in range(n):
    a, b = b, a+b 
  return a

def mfib(n): # top-down memoization
  if n<2: 
    return n
  L = [-1] * (n+1)    # not yet computed? set to -1
  L[0], L[1]  = 0, 1  # initialize two base values
  return rmf(n, L, n+1)  # helper function

def rmf(n, M, b):  # memoization helper function
  # assert(n < b)
  if M[n] < 0:
    fibn = rmf(n-1, M, b) + rmf(n-2, M, b)
    M[n] = fibn
  return M[n]

def fib_test(n):
  for j in range(n):
    f = fib(j)
    print j, f
    assert (f == ifib(j))
    assert (f == mfib(j))

def fib_demo(bign):
  print "\n ********** fib demo\n"
  t1 = 1.0
  for j in range(bign):
    now, fj = time.time(), fib(j)
    t0, t1  = t1, time.time()-now
    print j, fj, t1, "sec, ratio current/prev", t1/t0

def mfib_demo(bign):
  print "\n ********** mfib demo\n"
  t1 = 1.0
  for j in range(bign):
    print mfib(j)

def ifib_demo(x):
  print "\n ********* ifib demo\n"
  for _ in range(6):
    now = time.time()
    fx = ifib(x)
    print x, time.time() - now, "sec"
    x *= 2

fib_test(30)
fib_demo(35)
mfib_demo(35)
ifib_demo(40000)
