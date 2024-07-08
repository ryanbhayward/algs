# min weight rectilinear steiner tree    rbh 2024

# started :)

from operator import itemgetter as ig


def minmax(T): #min x-coord, min y, max x, max y
  return min(T, key=ig(0))[0],\
         min(T, key=ig(1))[1],\
         max(T, key=ig(0))[0],\
         max(T, key=ig(1))[1]

def report(T):
  print('\n', T, '\n', minmax(T), sep='')

T = ((0,5), (2,1), (4,7), (6,3))

report(T)
