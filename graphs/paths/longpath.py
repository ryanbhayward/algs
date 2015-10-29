# iterate over permutations
def characterList(x,y):
  
import itertools
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
  
def show(G):
  for v in sorted(G):
    print v,':',
    for j in G[v]: print j,
    print ''
  print ''

Verts = ['A','B','C','D','E','F']

G = {'A':['F','J'],
     'B':['D'],
     'C':['E'],
     'D':['G','I'],
     'E':['H'],
     'F':['G'],
     'G':['A','H'],
     'H':['E'],
     'I':['B','C','F'],
     'J':['C','F']}
scc(G)
