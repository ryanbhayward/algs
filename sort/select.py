def select(L,k):
  A = []; B = [];  C = []
  v = L[random.randint(0,len(L)-1)]
  for j in L:
    if j<v:
      A.append(j)
    elif j>v:
      C.append(j)
    else:
      B.append(j)
  if k <= len(A):
    return select(A,k)
  if k <= len(A) + len(B):
    return v
  return select(C,k-len(A)-len(B))
