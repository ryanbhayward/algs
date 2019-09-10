def collatz(n):
  while n > 1:
    print n,
    if n % 2 == 0:
      n = n / 2
    else:
      n = n * 3 + 1
  print n

def odd_collatz(n):
  while n > 1:
    if n % 2 == 0:
      n = n / 2
    else:
      print n,
      n = n * 3 + 1
  print n

for j in range(12):
  print ""
  collatz(2*j+1)
  odd_collatz(2*j+1)
