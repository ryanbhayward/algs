import sys
words = sys.stdin.readline().split()
A, B = words[0], words[1]
m, n = len(A),   len(B)
C = [[0 for y in range(n)] for x in range(m)]

for r in range(1,m): C[r][0] = r
for c in range(1,n): C[0][c] = c

for r in range(1,m):
  for c in range(1,n):
    t = C[r-1][c-1]
    if A[r] != B[c]: t+= 1
    C[r][c] = min(t, 1+C[r-1][c], 1+C[r][c-1])

for r in range(m):
  for c in range(n):
    print C[r][c],
  print ''
