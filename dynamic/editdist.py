import sys

words = sys.stdin.readline().split()
A, B = words[0], words[1]
m, n = len(A), len(B)
C = [[0 for y in range(n+1)] for x in range(m+1)]

for r in range(m): C[r+1][0] = r+1
for c in range(n): C[0][c+1] = c+1

for r in range(m):
  for c in range(n):
    t = C[r][c]
    if A[r] != B[c]: t+= 1
    C[r+1][c+1] = min(t, 1+C[r][c+1], 1+C[r+1][c])

print '    ',
for c in range(n): print B[c],
print ''
for r in range(m+1):
  if r==0: print '  ',
  else:    print A[r-1],'',
  for c in range(n+1):
    print C[r][c],
  print ''
