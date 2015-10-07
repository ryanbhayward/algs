def bitlength(n): return len(bin(n))-2

def leftright(x,n): # x > 1
  left  = x >> n/2
  right = x - (left << n/2)
  return left, right

def fastmul(x,y,depth): # x,y > 0
  for _ in range(depth):
    print '. ',
  print '(',x,y,')',bin(x),bin(y)
  n = bitlength(x)
  if n <= 4:
    return x*y
  xl, xr = leftright(x,n)
  yl, yr = leftright(y,n)
  pl = fastmul(xl,yl,1+depth)
  pr = fastmul(xr,yr,1+depth)
  pm = fastmul(xl+xr,yl+yr,1+depth)
  return (pl << 2*(n/2)) + ((pm - pl - pr) << n/2) + pr

fastmul(903,591,0)
