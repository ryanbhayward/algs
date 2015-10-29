def euclid(a,b): # a >= b >= 0
  print a,
  while b>0:
    a, b = b, a % b
    print a,
  print ''
  return a

euclid(9873,3627)
euclid(144,89)
