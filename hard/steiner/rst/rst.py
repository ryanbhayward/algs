# Ganley and Cohoon 94 FDP implementation    rbh 2024
# input: pins (terminal nodes) on rectilinear grid
#   format as per Zac's program
# output: min cost of steiner tree
#         (todo someday: also return edges)

from itertools import combinations
from sys import stdin
from string import ascii_uppercase
from operator import itemgetter as ig
from copy import deepcopy
from math import prod
from heapq import nlargest, nsmallest

def stringify(subset): # index subset to alphabetic string
  return ''.join(sorted([ascii_uppercase[j] for j in subset]))

def extract_subset(s, T): # index subset to sublist
  return [T[j] for j in s]

def tuples2lists(T): # when we want a mutable copy of T
  return [list(point) for point in T]

class Pins: # simple class of pins, a.k.a. terminal nodes
  def __init__(self):
    input_lines = []
    for line in stdin:
      input_lines.append(line.strip('\n'))
    self.n = int(input_lines[0])
    input_lines = input_lines[1:]
    assert(len(input_lines)==self.n)
    self.coords = []
    for j in range(self.n):
      pair = input_lines[j].split()
      self.coords.append((int(pair[0]), int(pair[1])))
    assert(self.n == len(self.coords))

def minmax(T): #min x-coord, min y, max x, max y
  return min(T, key=ig(0))[0],\
         min(T, key=ig(1))[1],\
         max(T, key=ig(0))[0],\
         max(T, key=ig(1))[1]

def spans(T):
  minx, miny, maxx, maxy = minmax(T)
  return maxx - minx, maxy - miny

def pointInList(t, T): # True if t in T
  for k in T:
    if t[0]==k[0] and t[1]==k[1]: 
      return True
  return False

def report(T, verbose):
  print(len(T), ' terminals\n', T, sep='') 
  if len(T) >= 3:
    if verbose: print('\ntuples')
    for j in range(1,4):
      for s in combinations(set(range(3)), j):
        if verbose: print(extract_subset(s, T))
  mnx, mny, mxx, mxy = minmax(T)
  xspan, yspan = mxx - mnx, mxy - mny
  if verbose:
    print('lower bound', xspan, "+", yspan, '=', xspan+yspan)
    print('fdp', fdp(T))
    print('caterpillar', caterpillar(T, verbose))

def rst4(K, verbose): # |K|==4: return cost of min-cost rst
  if verbose: print('rst4', K)
  assert(4==len(K))
  T = tuples2lists(K)
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
    if verbose: print('extras, xspan, yspan', extras, xspan, yspan)
  # using the shrink theorem: if side has exactly 1 pin,
  #   shrink from that pin until pin on another pin coordinate
  if T[-1][0] != T[-2][0]: # !1 pin on right side
    xshift = T[-1][0] - T[-2][0]
    T[-1][0] -= xshift
    if pointInList(T[-1], T[:-1]):
      return extras + xspan + yspan
    extras += xshift
    xspan  -= xshift
    if verbose: print('extras, xspan, yspan', extras, xspan, yspan)
  T = sorted(T, key=ig(1)) # now sort by y-coordinate
  if T[0][1] != T[1][1]: # !1 pin on bottom
    yshift = T[1][1] - T[0][1]
    T[0][1] += yshift
    if pointInList(T[0], T[1:]):
      return extras + xspan + yspan
    extras += yshift
    yspan  -= yshift
    if verbose: print('extras, xspan, yspan', extras, xspan, yspan)
  if T[-1][1] != T[-2][1]: # !1 pin on top
    yshift = T[-1][1] - T[-2][1]
    T[-1][1] -= yshift
    if pointInList(T[0], T[1:]):
      return extras + xspan + yspan
    extras += yshift
    yspan  -= yshift
    if verboase: print('extras, xspan, yspan', extras, xspan, yspan)
  return extras + xspan + yspan + min(xspan, yspan)

def rst234(T, verbose):
  if verbose: print('rst234')
  if len(T) < 4: 
    return sum(spans(T))
  return rst4(T, verbose)

def fdp(K): # return min cost
  n = len(K) # n >= 2
  if n <= 4: return rst234(K, False)

  # n >= 5: run Ganley Cohoon
  Rvals = {} # dictionary of terminal subset costs
  pin_Indices = set(range(n))
  for m in range(2, n+1):
    L = combinations(pin_Indices, m)
    for pin_sub in L:
      nameT = stringify(pin_sub)
      #print(nameT)
      T = extract_subset(pin_sub, K)
      if m <= 4: 
        Rvals[nameT] = rst234(T, False)
      # m >= 5
      #cost = caterpillar(T)
      Rvals[nameT] = caterpillar(T, True)
  return Rvals[stringify(pin_Indices)]

def cat_cost(t, T, ndx, span):
  return span[ndx] + sum([abs(q[1-ndx] - t[1-ndx]) for q in T])

def between(a, b, c):
  return (a < b and b < c) or (a > b and b > c)

def flip(T): # exchange x-y coordinates
  R = []
  for t in T:
    R.append((t[1],t[0]))
  return tuple(R)

def caterpillar(K, verbose): # 
  if verbose: print('\ncaterpillar')
  ss = spans(K)
  if prod(ss) == 0: return sum(ss)
  # bounding rectangle now has positive volume

  cost = float('inf')
  #V = tuples2lists(K) # another copy for vertical check
  
  H = deepcopy(K) # use to check for horizontal (bent)spine
  V = flip(K) # use to check for vertical   (bent)spine
  for T in [H, V]:
    print(T)
    mnx, mny, mxx, mxy = minmax(T)
    print(minmax(T))
    side_points = [[], []] # points on left and right sides of bound_rect
    ss = spans(T)
    for t in T:
      if   t[0] == mnx: side_points[0].append(t) # left side
      elif t[0] == mxx: side_points[1].append(t) # right 
    print('left side points:', end ='')
    for j in side_points[0]: print(j, end='')
    print()
    print('right side points:', end ='')
    for j in side_points[1]: print(j, end='')
    print()

    if len(side_points[0]) == 1: # spine from left
      pleft = side_points[0][0]  # unique point on left side
      current = cat_cost(pleft, T, 0, ss)
      cost = min(cost, current)
      print(cost)
      if (len(side_points[1]) == 1 and 
          pleft[1] != side_points[1][0][1]): # bent spine check
        pright = side_points[1][0] # unique point on right side
        xcoords = [p[0] for p in T]
        x2mn = nsmallest(2, xcoords)[1] # 2nd smallest x-coord
        x2mx = nlargest(2,  xcoords)[1] # 2nd  largest x-coord
        points_low, points_high = [], []
        for j in T:
          if j[0] == x2mn: points_low.append(j) # points, 2nd smallest x
          if j[0] == x2mx: points_high.append(j)#   "     2nd highest  x
        if len(points_high) == 1: # otherwise bent spine no better
          y0, y1, y2 = pleft[1], pright[1], points_high[0][1]
          x1, x2 = pright[0], points_high[0][0]
          if between(y0, y1, y2): 
            cost = min(cost, current - abs(y1 - y0))
            print('between', y0, y1, y2, cost)
        if len(points_low) == 1:
          y0, y1, y2 = pright[1], pleft[1], points_low[0][1]
          x1, x2 = pleft[0], points_low[0][0]
          if between(y0, y1, y2): 
            current = cat_cost(pright, T, 0, ss)
            cost = min(cost, current - abs(y1 - y0))
            print('between', y0, y1, y2, cost)
    if len(side_points[1]) == 1: # spine from right
      pright = side_points[1][0]
      cost = min(cost, cat_cost(pright, T, 0, ss))
    if verbose: print('cost so far', cost)
  return cost
      
P = Pins()
report(P.coords, True)

#for k in range(2, rst.n +1):
  #print(rst.n)
  #L = combinations(rst.pins,k)
  #M = []
  #for subset in L:
    #M.append(stringify(subset))
  #for subset in sorted(M):
    #print(subset)


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
          [[3,4], [0,0], [0,4], [3,0]],
          [[0,0], [4,0], [0,3], [4,3]],
          [[0,1], [1,0], [2,3], [3,2]],
          [[0,0], [1,0], [2,0], [3,0]],
          [[0,0], [0,3], [0,2], [0,1]],
          [[0,1], [1,4], [2,0], [3,2]],
        ]


#for T in Tvals:
#  print()
#  report(T)
