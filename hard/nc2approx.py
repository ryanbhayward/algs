#https://math.stackexchange.com/questions/58560/elementary-central-binomial-coefficient-estimates
from math import comb,log,floor,sqrt,pi

def lowbound(t):
  return 4**t / sqrt(pi*(t+1/3))

def upperbound(t):
  return 4**t / sqrt(pi*(t+.25))

for t in range(2, 21):
  n = 2*t
  print(n, floor(lowbound(t)), comb(n,t), floor(upperbound(t)))
