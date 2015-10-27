def test(G):
  s = {} 
  for v in G: s[v] = False
  for v in G:
    if not s[v]:
      ex(G,v,s)
      print ''

def ex(G,v,s):
  s[v] = True 
  print v,
  for w in G[v]:
    if not s[w]: ex(G,w,s)
  print v,

def show(G):
  for v in sorted(G):
    print v,':',
    for j in G[v]: print j,
    print ''

G = {'A':['E','I'], 'B':[], 'C':['D','E','F'], 'D':['H'], 'E':['G'],
     'F':['C','D'], 'G':['B','C'], 'H':['B','F'], 'I':['A','D']}
G = {'A':['I','E'], 'B':[], 'C':['F','E','D'], 'D':['H'], 'E':['G'],
     'F':['D','C'], 'G':['C','B'], 'H':['F','B'], 'I':['D','A']}
     
test(G)
