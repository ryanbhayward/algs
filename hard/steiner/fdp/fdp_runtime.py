from math import comb

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

for k in range(2, 11):
  print(k, '    ', fdp_time(k), formula(k))
  print()
