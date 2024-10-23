# min weight rectilinear steiner tree    rbh 2024

# working up to 4 terminals, woo hoo :)
# todo: 5 or more 
# todo: drop down to 3 and implement full-check (no-term-is-cutpoint)

from operator import itemgetter as ig

def minmax(T): #min x-coord, min y, max x, max y
  #print(T)
  #print('ig(0)', min(T, key=ig(0)))
  return min(T, key=ig(0))[0],\
         min(T, key=ig(1))[1],\
         max(T, key=ig(0))[0],\
         max(T, key=ig(1))[1]

def thinthick(T):
  minx, miny, maxx, maxy = minmax(T)
  return min(maxx - minx, maxy - miny), \
         max(maxx - minx, maxy - miny)

def showpairs(T):
  for pair in T:
    print(pair[0], pair[1], ' ', end='')
  print()

def report(T):
  showpairs(T)
  print(' ', rst(T))

def rst(T): # min wt rect steinter tree
  n = len(T)
  if n == 1:
    return 0
  if n == 2 or n ==3:
    return sum(thinthick(T))
  if n == 4:
    xsorted = sorted(T, key=ig(0))
    ysorted = sorted(T, key=ig(1))
    #print('x sorted', xsorted)
    #print('y sorted', ysorted)
    if xsorted[0][0] != xsorted[1][0]:
      xshift = xsorted[1][0] - xsorted[0][0]
      xsorted[0][0] += xshift
      print('  shift right', xshift)
      return xshift + rst(xsorted)
    elif xsorted[-1][0] != xsorted[-2][0]:
      xshift = xsorted[-1][0] - xsorted[-2][0]
      xsorted[-1][0] -= xshift
      print('  shift left', -xshift)
      return xshift + rst(xsorted)
    elif ysorted[0][1] != ysorted[1][1]:
      yshift = ysorted[1][1] - ysorted[0][1]
      ysorted[0][1] += yshift
      print('  shift up', yshift)
      return yshift + rst(ysorted)
    elif ysorted[-1][1] != ysorted[-2][1]:
      yshift = ysorted[-1][1] - ysorted[-2][1]
      ysorted[-1][1] -= yshift
      print('  shift down', -yshift)
      return yshift + rst(ysorted)
    else:
      thin, thick = thinthick(T)
      return thin + thin + thick
  else: assert False

Tvals = [ [[6,3], [0,5], [2,1], [4,7]],
          [[6,3]],
          [[6,3], [0,5]],
          [[6,3], [6,2]],
          [[6,3], [0,3]],
          [[6,3], [0,5], [2,1]],
          [[0,0], [0,4], [3,0], [3,4]],
          [[0,0], [4,0], [0,3], [4,3]] 
        ]

for T in Tvals:
  report(T)
