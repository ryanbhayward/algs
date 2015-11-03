import sys

def getStrings():
  print 'strings:  ',
  words = sys.stdin.readline().split()
  return words[0], words[1]

A, B = getStrings()
m, n = len(A), len(B)

# track edit distance of prefixes
# best alignment of A[1..i], B[1..j] ?
#  A[1.. i ]   -
#  B[1..j-1]  B[j]       
#                        or
#  A[1..i-1]  A[j]
#  B[1.. j ]   -         
#                        or
#  A[1..i-1]  B[i]
#  B[1..j-1]  A[j]
#
#  C[i][j]: best of above 3

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
