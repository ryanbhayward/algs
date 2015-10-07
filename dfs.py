def dfs(G):
  seen = {}
  for v in G: seen[v] = False
  for v in G:
    if not seen[v]:
      explore(G,v,seen)

def explore(G,v,seen):
  print v, 'start explore'
  seen[v] = True
  for nbr in G[v]:
    if not seen[nbr]:
      explore(G,nbr,seen)
  print v, 'finish explore'

def show(G):
  for v in sorted(G):
    print v,':',
    for j in G[v]: print j,
    print ''
  print ''

G = {'A': ['C', 'E', 'F'],
     'B': ['G', 'H'],
     'C': ['A', 'F'],
     'D': [],
     'E': ['A', 'F'],
     'F': ['A', 'C', 'E'],
     'G': ['B', 'H'],
     'H': ['B', 'G']}

show(G)

dfs(G)
