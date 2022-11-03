#!/usr/bin/env python3
def collatz(n):
  print(n, end=': ')
  while n > 1:
    print(n, end=' ')
    if n % 2 == 0: n = n // 2
    else: n = n*3 + 1
  print(n)

def odd_collatz(n):
  while n > 1:
    if n % 2 == 0: n = n // 2
    else:
      print(n, end=' ')
      n = n*3 + 1
  print(n)

for j in range(1,50):
  odd_collatz(2*j+1)
  print('')
