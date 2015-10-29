def modexp(x,y,n): #integers, y >= 0, n >= 2
  if y==0:
    return 1
  z = modexp(x,y/2,n)
  if 0==y%2:
    return (z*z)%n
  else:
    return (x*z*z)%n

for j in range(-5,5):
  for k in range(10):
    for m in range(10):
      assert modexp(j,k,m+2)==pow(j,k,m+2)
