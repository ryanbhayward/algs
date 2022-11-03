# simple astar 
import weight3
def astar(G,source, target):
  infinity = weight3.infinity(G)
  dist, priority, heuristic, parent, fringe, done = {}, {}, {}, {}, [], []
  for v in G:
    dist[v], priority[v], parent[v] = infinity, infinity, -1
  dist[source], priority[source], parent[source] = 0, 0, source

  #nodes, hvals = ['A','B','C','Z'], [0, 20, 22, 0]
  #              [  0, 26, 24, 22, 18,  7, 10, 0 ]
  #              [  0, 26, 25, 20, 17,  7, 10, 0 ]
  #              [  0, 26, 24, 22, 18,  7,  2, 0 ]
  #              [  0, 26, 25, 22, 17,  7,  2, 0 ]
  #              [  0, 26, 24, 22,  2,  7, 10, 0 ]
  nodes, hvals = ['A','B','C','D','E','F','G','Z'],\
                 [  0, 26, 25, 22,  2,  7, 10, 0 ]
  assert len(nodes)==len(hvals)
  for j in range(len(nodes)): heuristic[nodes[j]] = hvals[j]
  for j in range(len(nodes)): print(nodes[j], heuristic[nodes[j]])

  msg = '*'
  fringe.append(source)
  while len(fringe) > 0:
    current = fringe.pop(weight3.indexOfMin(fringe, priority))
    done.append(current)
    print('current', current, 'priority', priority[current])
    msg = msg + current + '*' + str(priority[current]) + '*'
    if current == target: break
    for (v, wuv) in G[current]:
      if v not in done:
        new_v_dist = dist[current] + wuv
        if new_v_dist < dist[v]:
          dist[v] = new_v_dist
          parent[v] = current
          priority[v] = new_v_dist + heuristic[v]
          if v not in fringe: fringe.append(v)

  print(msg)
  print('')

#G = weight3.G8
G = weight3.G9
print(G)
astar(G,'A','Z')
