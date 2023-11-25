### create distance dictionary of complete graph on towns rbh 2022
from sys import stdin

def init_distance_dict(verbose):
  # read n, inter-city distances from stdin
  D = []
  for line in stdin:
    for word in line.split():
      D.append(int(word))
  n = D.pop(0)                 # first integer is number of towns
  assert(len(D) == n*(n-1)/2)  # complete graph, so this many pairs
  towns = [t for t in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:n]]

  ndx, dist, n = 0, {}, len(towns)
  for j in range(n):
    t = towns[j]
    dist[t] = {}
    for k in range(j+1,n):
      u = towns[k]
      dist[t][u] = D[ndx]
      ndx += 1

  # add reverse edges
  for t in towns:
    for nbr in dist[t]:
      if t not in dist[nbr]:
        dist[nbr][t] = dist[t][nbr]

  # pretty output
  if verbose:
    for t in towns:
      print(t, end=': ')
      for u in towns:
        if u in dist[t]:
          print('{:3}'.format(dist[t][u]), end='  ')
        else:
          print('     ', end='')
      print('')

  return dist

init_distance_dict(True)
