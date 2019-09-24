# recursive formula for number of binary search trees
# also known as Catalan numbers
def cat(n):
  C = [1,1,2]
  for j in range(3,n+1):
    s = 0
    for k in range(j):
      s += C[k]*C[j-(1+k)]
    C.append(s)
  return C

L = cat(10)
print L
