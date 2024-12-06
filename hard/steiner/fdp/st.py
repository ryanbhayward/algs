# min weight rectilinear steiner tree    rbh 2024

# working up to 4 terminals, woo hoo :)
# todo: 5 or more 
# todo: drop down to 3 and implement full-check (no-term-is-cutpoint)
#   conjecture: if no-term-is-cut and
#     for bounding rectangle, 
#       *each side has at least 2 terminals,
#        then full caterpillar has straight spine
#       *some side has only a terminal,
#        then shift the terminal inside 1 unit (after adding the edge)
#        I think this allows us to skip the bent-spine case

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
      print('  shift from left', xshift)
      return xshift + rst(xsorted)
    elif xsorted[-1][0] != xsorted[-2][0]:
      xshift = xsorted[-1][0] - xsorted[-2][0]
      xsorted[-1][0] -= xshift
      print('  shift from right', xshift)
      return xshift + rst(xsorted)
    elif ysorted[0][1] != ysorted[1][1]:
      yshift = ysorted[1][1] - ysorted[0][1]
      ysorted[0][1] += yshift
      print('  shift from bottom', yshift)
      return yshift + rst(ysorted)
    elif ysorted[-1][1] != ysorted[-2][1]:
      yshift = ysorted[-1][1] - ysorted[-2][1]
      ysorted[-1][1] -= yshift
      print('  shift from top', yshift)
      return yshift + rst(ysorted)
    else:
      thin, thick = thinthick(T)
      return thin + thin + thick
  else: assert False

Tvals = [ 
          [[0,0], [5,0], [0,4], [1,1]],
          [[5,0], [0,0], [5,4], [4,1]],
          [[0,0], [5,0], [0,4], [3,1]],
          [[0,0], [5,0], [0,4], [1,3]],
          [[0,0], [5,0], [0,4], [7,3]],
          [[0,0], [5,0], [0,4], [3,7]],
          [[3,6], [5,0], [1,2], [7,4]],
          [[6,3], [0,5], [2,1], [4,7]],
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
