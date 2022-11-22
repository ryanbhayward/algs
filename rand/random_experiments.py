import numpy as np

def trial(n):
  return np.random.permutation(n)

n = 7
A, B, C = {0, 1, 2}, {3, 4, 5}, {6}

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
