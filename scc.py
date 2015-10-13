def dfs(G,v,seen,cmpt,c,S,phase):
  seen[v],cmpt[v] = True,c
  for nbr in sorted(G[v]):
    if not seen[nbr]: dfs(G,nbr,seen,cmpt,c,S,phase)
  if (phase==0): S.append(v) # append in postorder

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
    if not seen[v]: dfs(T,v,seen,cmpt,c,S,phase)
  showall(T,cmpt,S)

  phase,c = 1,0
  for v in G: seen[v],cmpt[v] = False, 0
  while len(S)>0:
    v = S.pop()
    if not seen[v]:   
      c += 1
      dfs(G,v,seen,cmpt,c,S,phase)
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


G = {'A':['F'],
     'B':['H'],
     'C':['B','F'],
     'D':['I'],
     'E':['B'],
     'F':['C','I'],
     'G':['E'],
     'H':['G'],
     'I':['A','G']}
scc(D2)
