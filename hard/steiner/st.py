# min weight rectilinear steiner tree    rbh 2024

# started
# correct if at most 3 terminals :)
# todo: what if 4 or more terminals?

from operator import itemgetter as ig


def minmax(T): #min x-coord, min y, max x, max y
  return min(T, key=ig(0))[0],\
         min(T, key=ig(1))[1],\
         max(T, key=ig(0))[0],\
         max(T, key=ig(1))[1]

def report(T):
  print('\n', T, '\n', minmax(T), sep='')
  print(rst(T))

def rst(T): # min wt rect steinter tree
  n = len(T)
  if n == 1:
    return 0
  minx, miny, maxx, maxy = minmax(T)
  thin = min(miny - minx, maxy - maxx)
  thick = max(miny - minx, maxy - maxx)
  if n == 2 or n ==3:
    return thin + thick
  if n == 4:
    return thin + thin + thick
  else: assert False

T = ((0,5), (2,1), (4,7), (6,3))

report(T)
