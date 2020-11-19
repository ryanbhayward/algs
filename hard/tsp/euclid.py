#!/usr/local/bin/python3
# rbh 2020
# input: nodes on the x-y Cartesian plane
# output: array of node-node distances, rounded to integer
# input format:
#   - one node per line: name, x-coord, y-coord
#   - e.g.
#     A  13 24
#     B  -6 11

from sys import stdin
from math import sqrt

def read_nodes():
  N = []
  for line in stdin:
    #node = line.strip()
    node = line.strip().split()
    N.append( (node[0], int(node[1]), int(node[2])) )
  return N

def dist(a, b, c, d, scale):
  return( round(sqrt((a-c)*(a-c)+(b-d)*(b-d)) / scale) )

def all_dist(N):
  n = len(N)
  print('   ', end='')
  for j in range(1, n):
    print('  ' + N[j][0], end='')
  print('')
  for j in range(n-1):
    print(N[j][0] + ':', end='  ')
    for k in range(j+1, n):
      print('{:2d}'.format(dist(N[j][1], N[j][2], N[k][1], N[k][2], 9.0)), end=' ')
    print('')

N = read_nodes()
for v in N:
  print(v[0], v[1], v[2])
all_dist(N)
