# run randomized kruskal min cut t times
# prob(success) on 1 trial >= 2/(n(n-1))
# rbh 2022
def success_bound(n):
  return 2.0 / (n * (n - 1.0))

def fail_prob(sbound, t):
  return pow(1.0 - sbound, t)

def onepercent(sbound):
  t = 1
  while fail_prob(sbound, t) > 0.01:
    t += 1
  return t

#n, sbound, trials = 6, 13.0/35.0, 10
n = 100
sbound = success_bound(n)

#trials = 10
#for t in range(1, trials+1):
#  print(1.0 - fail_prob(sbound, t))

print(onepercent(sbound))
