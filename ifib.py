def ifib(n):
  a,b = 0,1
  for _ in range(n):
    a, b = b, a+b    #
  return a

x = 40000
for _ in range(6):
  now = time.time()
  fx = ifib(x)
  print x, time.time() - now, "sec"
  x *= 2
