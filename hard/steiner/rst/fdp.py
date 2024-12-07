# implementation of Ganley and Cohoon 94     rbh 2024
# input: terminal nodes on rectilinear grid
# input format: same as Zac's program,
# output: min cost of steiner tree

# todo: also return edges (haha ... this will never happen :)
# todo: caterpillar looks ok, now final loops :)

# use Zac's program if you want to see a solution (not nec. this one)

from itertools import combinations
from sys import stdin
from string import ascii_uppercase
from operator import itemgetter as ig
from copy import deepcopy

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
    self.coords, self.pins = [], set()  # pins: labels for terminals
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

def spans(T):
  minx, miny, maxx, maxy = minmax(T)
  return maxx - minx, maxy - miny

def showpoints(T):
  for point in T:
    print(point[0], point[1], ' ', end='')
  print()

def pointInList(t, T): # true if t in T
  for k in T:
    if t[0]==k[0] and t[1]==k[1]: 
      return True
  return False

def report(T):
  showpoints(T)
  mnx, mny, mxx, mxy = minmax(T)
  xspan, yspan = mxx - mnx, mxy - mny
  print('lower bound', xspan, "+", yspan, '=', xspan+yspan)
  print('fdp', fdp(T))
  print('caterpillar', caterpillar(T))

def rst4(K): # K has size 4: return min cost of rst
  assert(4==len(K))
  T = deepcopy(K)
  xspan, yspan = spans(T)
  extras = 0 # number edges added as we shrink T
  T = sorted(T, key=ig(0)) # sort by x-coordinate
  if T[0][0] != T[1][0]: #  !1 pin on left side
    xshift = T[1][0] - T[0][0]
    T[0][0] += xshift
    if pointInList(T[0], T[1:]):
      return xspan + yspan
    extras += xshift
    xspan  -= xshift
    print('extras, xspan, yspan', extras, xspan, yspan)
  # using the shrink theorem: if any side has exactly 1 pin,
  #   then shrink that edge until it hits another pin coordinate
  if T[-1][0] != T[-2][0]: # !1 pin on right side
    xshift = T[-1][0] - T[-2][0]
    T[-1][0] -= xshift
    if pointInList(T[-1], T[:-1]):
      return extras + xspan + yspan
    extras += xshift
    xspan  -= xshift
    print('extras, xspan, yspan', extras, xspan, yspan)
  T = sorted(T, key=ig(1)) # now sort by y-coordinate
  if T[0][1] != T[1][1]: # !1 pin on bottom
    yshift = T[1][1] - T[0][1]
    T[0][1] += yshift
    if pointInList(T[0], T[1:]):
      return extras + xspan + yspan
    extras += yshift
    yspan  -= yshift
    print('extras, xspan, yspan', extras, xspan, yspan)
  if T[-1][1] != T[-2][1]: # !1 pin on top
    yshift = T[-1][1] - T[-2][1]
    T[-1][1] -= yshift
    if pointInList(T[0], T[1:]):
      return extras + xspan + yspan
    extras += yshift
    yspan  -= yshift
    print('extras, xspan, yspan', extras, xspan, yspan)
  return extras + xspan + yspan + min(xspan, yspan)

def fdp(T): # return min cost
  Rvals = {} 
  # dictionary of terminal subset rst costs
  # keys will be subset stringified, e.g.
  #   subset {A, D, E} => key 'ADE'
  n = len(T)
  if n == 1:           return 0
  if n == 2 or n == 3: return sum(spans(T))
  if n == 4:           return rst4(T)
  else:                return -1
  # if there are more than 4 terminals, run Ganley Cohoon

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
  tt = spans(K)
  if tt[0] == 0 or tt[1] == 0: return sum(tt)

  # now bounding rectangle has positive volume
  for T in [K, flip(K)]:
    mnx, mny, mxx, mxy = minmax(T)
    side_points = [[], []] # points on left and right sides of bound_rect
    spansT = spans(T)
    for t in T:
      if   t[0] == mnx: side_points[0].append(t) # left side
      elif t[0] == mxx: side_points[1].append(t) # right 
    if len(side_points[0]) == 1: # spine from left
      pleft = side_points[0][0]
      print('pleft', pleft)
      cost = min(cost, cat_cost(pleft, T, 0, spansT))
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
      cost = min(cost, cat_cost(pright, T, 0, spansT))
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
#          [[0,0], [5,0], [0,4], [1,2]],
#          [[0,0], [5,0], [0,4], [2,1]],
#          [[5,0], [0,0], [5,4], [4,1]],
#          [[0,0], [5,0], [0,4], [3,1]],
#          [[0,0], [5,0], [0,4], [1,3]],
#          [[0,0], [5,0], [0,4], [7,3]],
#          [[0,0], [5,0], [0,4], [3,7]],
#          [[3,6], [5,0], [1,2], [7,4]],
#          [[6,3], [0,5], [2,1], [4,7]],
#         [[6,3]],
          [[6,3], [0,5]],
          [[6,3], [6,2]],
          [[6,3], [0,3]],
          [[6,3], [0,5], [2,1]],
          [[0,0], [0,4], [3,0], [3,4]],
          [[0,0], [4,0], [0,3], [4,3]],
          [[0,1], [1,0], [2,3], [3,2]],
          [[0,0], [1,0], [2,0], [3,0]],
          [[0,0], [0,3], [0,2], [0,1]],
          [[0,1], [1,4], [2,0], [3,2]],
        ]

for T in Tvals:
  print()
  report(T)
