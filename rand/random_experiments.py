import numpy as np
# simple random simulations to confirm
#   probabilities for randomized min cut
#   rbh 2022


def trial(n): # random perm of {0, ..., n-1}
  return np.random.permutation(n)

# -randomized Kruskal min cut:
#   -- execute Kruskal on graph, selecting edges uni-random
#   -- stop when number of components is 2 (this is the cut)
# -probability that RKMC is min cut is at least 1/(n*(n-1))
# -you can work out these probs exactly for small graphs
# e.g. define G: triangle edges 0,1,2, 
#                  triangle edges 3,4,5,
#                  and single edge 6 between 2 triangles
# -prob that RKMC finds min cut =
#    prob that edge 6 is last in random edge perm or
#    prob that edge 6 is 2nd last " "  or
#    prob that edge 6 is 3nd last and last two edges are from diff't triangles
# = 1/7 + 1/7 + (1/7)(3/5) = 13/35 = .371...

# this simulation confirms this arithmetic

n, A, B, C = 7, {0, 1, 2}, {3, 4, 5}, {6}

def mincut(p):
  return (p[6] in C) or (p[5] in C) or (
            p[4] in C and (
              (p[5] in A and p[6] in B) or (
               p[5] in B and p[6] in A)))

hits, trials = 0, 100000
for _ in range(trials):
  j = trial(n)
  if mincut(j):
    hits += 1
print(hits, trials, 'hits, trials')
