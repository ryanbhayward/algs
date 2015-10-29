def dfs(G,v,seen,cmpt,c,S,phase):
  seen[v],cmpt[v] = True,c
  for nbr in sorted(G[v]):
    if not seen[nbr]: dfs(G,nbr,seen,cmpt,c,S,phase)
  if (phase==0): S.append(v) # append in postorder
  print v,

def transpose(G):
  T = {}
  for v in G: T[v] = []
  for v in G: 
    for w in G[v]: T[w].append(v)
  return T

def scc(G):
  phase,seen,cmpt,c,S = 0,{},{},0,[]
  for v in G: seen[v],cmpt[v] = False, 0
  T = transpose(G)
  for v in sorted(T):
    if not seen[v]: 
      dfs(T,v,seen,cmpt,c,S,phase)
  print ''
  showall(T,cmpt,S)

  phase,c = 1,0
  for v in G: seen[v],cmpt[v] = False, 0
  while len(S)>0:
    v = S.pop()
    if not seen[v]:   
      c += 1
      print 'scc',c,':',
      dfs(G,v,seen,cmpt,c,S,phase)
      print ''
  print ''
  showall(G,cmpt,S)

def showall(G,cmpt,S):
  print '     ',
  for v in sorted(G): print '%2s' % v,
  print '\ncmpt ',
  for v in sorted(G): print '%2s' % cmpt[v],
  print '\nstack', S
  
D = { 'A':['B'],
      'B':['C','E','F'],
      'C':['D','G'],
      'D':['C','H'],
      'E':['A','F'],
      'F':['G'],
      'G':['F'],
      'H':['D','G']
}

D2 = {'A':['G'],
      'B':['E'],
      'C':['L'],
      'D':[],
      'E':['B','H'],
      'F':['A','H'],
      'G':['F'],
      'H':['B','I'],
      'I':['E'],
      'J':[],
      'K':['C'],
      'L':['K']
}

D3 = {'A':['B'],
      'B':['C','E','F'],
      'C':['B','D','G'],
      'D':['H'],
      'E':['A','F','I'],
      'F':['I'],
      'G':['F','H','K'],
      'H':['K'],
      'I':['J'],
      'J':['F'],
      'K':['J','L'],
      'L':['H']
}

D4 = {'A':['E'],
      'B':['A','C'],
      'C':['G'],
      'D':['C'],
      'E':['B','I'],
      'F':['B','E','G'],
      'G':['D'],
      'H':['D','G','L'],
      'I':['E'],
      'J':['F','I','K'],
      'K':['G','H','J'],
      'L':['K']
}

G = {'A':['F'],
     'B':['H'],
     'C':['B','F'],
     'D':['I'],
     'E':['B'],
     'F':['C','I'],
     'G':['E'],
     'H':['G'],
     'I':['A','G']}
scc(D4)
