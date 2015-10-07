def ms(x): # based on:
#http://stackoverflow.com/questions/18761766/mergesort-python
  result = []
  if len(x) < 2:
    return x
  mid = len(x)/2 ; y = ms(x[:mid]) ; z = ms(x[mid:])
  i,j = 0,0
  while i < len(y) and j < len(z):
    if y[i] > z[j]:
      result.append(z[j]) ; j += 1
    else:
      result.append(y[i]) ; i += 1
  result += y[i:] + z[j:]
  return result
