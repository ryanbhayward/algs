# implementation of Ganley and Cohoon 94     rbh 2024
# input: terminal nodes on rectilinear grid
# output: min cost of steiner tree

# todo: also return edges (haha ... this will never happen :)
# todo: caterpillar looks ok, now final loops :)

# takes input in format used by Zac's program,
# use Zac's program if you want to see a solution (not nec. this one)

from itertools import combinations
from sys import stdin
from string import ascii_uppercase
from operator import itemgetter as ig

def stringify(S): # characters to alphabetic string
  return ''.join(sorted(S))

class RST: # simple RST class
  def __init__(self):
    input_lines = []
    for line in stdin:
      input_lines.append(line.strip('\n'))
    self.n = int(input_lines[0])
    input_lines = input_lines[1:]
    assert(len(input_lines)==self.n)
    print(self.n, 'terminals')
    self.coords, self.pins = [], set()
    for j in range(self.n):
      pair = input_lines[j].split()
      self.coords.append((int(pair[0]), int(pair[1])))
      self.pins.add(ascii_uppercase[j])
    assert(self.n == len(self.coords))
    assert(self.n == len(self.pins))
    print('coordinates', self.coords)
    print('pins', self.pins)

def minmax(T): #min x-coord, min y, max x, max y
  return min(T, key=ig(0))[0],\
         min(T, key=ig(1))[1],\
         max(T, key=ig(0))[0],\
         max(T, key=ig(1))[1]

def thinthick(T):
  minx, miny, maxx, maxy = minmax(T)
  return min(maxx - minx, maxy - miny), \
         max(maxx - minx, maxy - miny)

def showpoints(T):
  for pair in T:
    print(pair[0], pair[1], ' ', end='')
  print()

def report(T):
  showpoints(T)
  mnx, mny, mxx, mxy = minmax(T)
  xspan, yspan = mxx - mnx, mxy - mny
  print('lower bound', xspan, "+", yspan, '=', xspan+yspan)
  print('fdp', fdp(T))
  print('caterpillar', caterpillar(T))

def case_4(T): # return min cost
  assert(4==len(T))# T has four nodes, possible duplicate nodes
  xsorted = sorted(T, key=ig(0))
  ysorted = sorted(T, key=ig(1))
  if xsorted[0][0] != xsorted[1][0]:
    xshift = xsorted[1][0] - xsorted[0][0]
    xsorted[0][0] += xshift
    #print('  shift from left', xshift)
    return xshift + case_4(xsorted)
  elif xsorted[-1][0] != xsorted[-2][0]:
    xshift = xsorted[-1][0] - xsorted[-2][0]
    xsorted[-1][0] -= xshift
    #print('  shift from right', xshift)
    return xshift + case_4(xsorted)
  elif ysorted[0][1] != ysorted[1][1]:
    yshift = ysorted[1][1] - ysorted[0][1]
    ysorted[0][1] += yshift
    #print('  shift from bottom', yshift)
    return yshift + case_4(ysorted)
  elif ysorted[-1][1] != ysorted[-2][1]:
    yshift = ysorted[-1][1] - ysorted[-2][1]
    ysorted[-1][1] -= yshift
    #print('  shift from top', yshift)
    return yshift + case_4(ysorted)
  else:
    thin, thick = thinthick(T)
    return thin + thin + thick

def fdp(T): # return min cost
  n = len(T)
  if n == 1:           return 0
  if n == 2 or n == 3: return sum(thinthick(T))
  if n == 4:           return case_4(T)
  else:                return -1

def cat_cost(t, T, ndx, span):
  return span[ndx] + sum([abs(q[1-ndx] - t[1-ndx]) for q in T])

def between(a, b, c):
  return (a < b and b < c) or (a > b and b > c)

def flip(T): # exchange x-y coordinates
  R = []
  for t in T:
    R.append((t[1],t[0]))
  return R

def caterpillar(K): # 
  cost = float('inf')
  tt = thinthick(K)
  if tt[0] == 0 or tt[1] == 0: return sum(tt)

  # now bounding rectangle has positive volume
  for T in [K, flip(K)]:
    mnx, mny, mxx, mxy = minmax(T)
    side_points = [[], []] # points on left and right sides of bound_rect
    span = [mxx - mnx, mxy - mny]
    for t in T:
      if   t[0] == mnx: side_points[0].append(t) # left side
      elif t[0] == mxx: side_points[1].append(t) # right 
    if len(side_points[0]) == 1: # spine from left
      pleft = side_points[0][0]
      print('pleft', pleft)
      cost = min(cost, cat_cost(pleft, T, 0, span))
      if (len(side_points[1]) == 1 and 
             side_points[0][0][1] != side_points[1][0][1]): # bent spine check
        pright = side_points[1][0]
        print('pright', pright)
        low, high = mxx, mnx
        for j in T:
          if j[0] > high and j[0] < mxx: high = j[0] # better high
          if j[0] < low  and j[0] > mnx: low = j[0]  # better low
        points_low, points_high = [], []
        for j in T:
          if j[0] == low:  points_low.append(j) # points with 2nd smallest x
          if j[0] == high: points_high.append(j)#   " 2nd highest x
        if len(points_high) == 1:
          y0, y1, y2 = pleft[1], pright[1], points_high[0][1]
          x1, x2 = pright[0], points_high[0][0]
          if between(y0, y1, y2): cost -= abs(y1 - y0)
        if len(points_low) == 1:
          y0, y1, y2 = pright[1], pleft[1], points_low[0][1]
          x1, x2 = pleft[0], points_low[0][0]
          if between(y0, y1, y2): cost -= abs(y1 - y0)
    if len(side_points[1]) == 1: # spine from right
      pright = side_points[1][0]
      cost = min(cost, cat_cost(pright, T, 0, span))
    print('cost so far', cost)
  return cost
      
rst = RST()

for k in range(2, rst.n +1):
  print(rst.n)
  L = combinations(rst.pins,k)

  M = []
  for subset in L:
    M.append(stringify(subset))
  for subset in sorted(M):
    print(subset)

report(rst.coords)

Tvals = [
#          [[0,0], [5,0], [0,4], [1,1]],
#          [[5,0], [0,0], [5,4], [4,1]],
#          [[0,0], [5,0], [0,4], [3,1]],
#          [[0,0], [5,0], [0,4], [1,3]],
#          [[0,0], [5,0], [0,4], [7,3]],
#          [[0,0], [5,0], [0,4], [3,7]],
#          [[3,6], [5,0], [1,2], [7,4]],
#          [[6,3], [0,5], [2,1], [4,7]],
#          [[6,3]],
#          [[6,3], [0,5]],
#          [[6,3], [6,2]],
#          [[6,3], [0,3]],
#          [[6,3], [0,5], [2,1]],
#          [[0,0], [0,4], [3,0], [3,4]],
          [[0,1], [1,0], [2,3], [3,2]]
#          [[0,0], [4,0], [0,3], [4,3]]
        ]

#for T in Tvals:
#  print()
#  report(T)

