from math import comb
from itertools import combinations
from sys import stdin
from string import ascii_uppercase

# checking the formula for runtime from Ganley and Cohoon 1994 paper
# number of line executions of FDP(T)
def fdp_time(k): # k number of terminals
  count = 0
  for m in range(2, k+1):
    val = comb(k, m) * m * 2**(m-1)
    print(m, val)
    count += val
  return count

# formula given in paper has a typo, it forgets to subtract k
def formula(k):
  return k * (3**(k-1) - 1)

#for k in range(2, 11):
#  print(k, '    ', fdp_time(k), formula(k))
#  print()

class RST: # simple RST class
  def __init__(self):
    L = []
    for line in stdin:
      L.append(line.strip('\n'))
    self.n = int(L[0])
    L = L[1:]
    assert(len(L)==self.n)
    print(self.n, 'terminals')
    self.coords, self.pins = [], set()
    for j in range(self.n):
      pair = L[j].split()
      self.coords.append((int(pair[0]), int(pair[1])))
      self.pins.add(ascii_uppercase[j])
    assert(self.n == len(self.coords))
    assert(self.n == len(self.pins))
    print('coordinates', self.coords)
    print('pins', self.pins)

rst = RST()

for k in range(2,rst.n+1):
  print(rst.n)
  L = combinations(rst.pins,k)

  M = []
  for j in L:
    M.append(''.join(sorted(j)))
  for j in sorted(M):
    print(j)
