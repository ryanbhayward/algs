import sys

def getStrings():
  print 'strings:  ',
  words = sys.stdin.readline().split()
  return words[0], words[1]

A, B = getStrings()
m, n = len(A), len(B)

C = [[0 for y in range(n+1)] for x in range(m+1)]
for r in range(m): C[r+1][0] = r+1
for c in range(n): C[0][c+1] = c+1
for r in range(m):
  for c in range(n):
    t = C[r][c]
    if A[r] != B[c]: t+= 1
    C[r+1][c+1] = min(t, 1+C[r][c+1], 1+C[r+1][c])

print '\n      ',
for c in range(len(B)): print B[c],
print '\n'
S = ' ' + A
for r in range(len(S)):
  print '',S[r],' ',
  for c in range(n+1):
    print C[r][c],
  print ''
