def exteuclid(a,b): #a>=b>=0: x,y,d: ax+by=d=gcd(a,b)
  if b==0:
    print a,'* 1 +',b,'* 0 =',a
    return 1, 0, a
  x, y, d = exteuclid(b, a%b)
  print a,'*',y,'+',b,'*',x-(a/b)*y,'=',d
  return y, x-(a/b)*y, d

exteuclid(8616909,135716)
