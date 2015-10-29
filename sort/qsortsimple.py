def pn(list,start,end): # simple partition
  A,B = [], []
  pivot = list[start]
  for j in range(start+1,end+1):
    if list[j] < pivot: A.append(list[j])
    else:               B.append(list[j])
  a = len(A)
  for j in range(a): L[start+j] = A[j]
  L[start+a] = pivot
  for j in range(len(B)): L[start+j+a+1] = B[j]
  return start+a

def qsort(list, start, end):
  print start,end,
  if start < end:  
    print L
    split = pn(list, start, end)
    qsort(list, start, split-1)
    qsort(list, split+1, end)
  else: print ''

L = [44,88,11,0,33,99,22,77,66,55]
qsort(L,0,len(L)-1)
