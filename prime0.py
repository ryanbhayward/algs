def isprime(n):
  for j in range(2,n):
    if 0==n%j:
      return False  # composite
  return True      # prime

for t in range(2, 1000):
  if isprime(t):
    print t
