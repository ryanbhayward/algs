# simple factoring
import sys
n = int(sys.stdin.readline().strip())
print 'nontrivial divisors:', 
for j in range(2,n):
  if n%j == 0: print j, n/j,
  if j*j>=n: break
print ''
