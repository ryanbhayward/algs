# simple a-star 
import weight3 # weighted graph input, IO

# target     final destination
# wuv        weight(u,v): roadmap distance of edge (u,v)
# est_ttl    estimated total distance (dist-so-far + heuristic) to dest'n
# hrstc      heuristic
# dist[v]    dist-so-far from source to v
#                 - at end, will be length of shortest-path-found
#                   ... and if hrstc never overestimates distance,
#                   dist will be true distance (length of shortest path)

def astar(G,source, target):
  infty = weight3.infinity(G)
  dist, est_ttl, hrstc, parent, fringe, done = {}, {}, {}, {}, [], []
  for v in G:
    dist[v], est_ttl[v], parent[v] = infty, infty, -1
  dist[source], est_ttl[source], parent[source] = 0, 0, source

  nodes, hvals = ['A','B','C','D','E','F','G','Z'],\
                 [  0, 26, 25, 22,  2,  7, 10, 0 ]
  assert len(nodes)==len(hvals)
  for j in range(len(nodes)): hrstc[nodes[j]] = hvals[j]
  for j in range(len(nodes)): print(nodes[j], hrstc[nodes[j]])

  msg = '*'
  fringe.append(source)
  while len(fringe) > 0:
    current = fringe.pop(weight3.indexOfMin(fringe, est_ttl))
    done.append(current)
    print('current', current, 'est_ttl', est_ttl[current])
    msg = msg + current + '*' + str(est_ttl[current]) + '*'
    if current == target: break
    for (v, wuv) in G[current]:
      if v not in done:
        new_v_dist = dist[current] + wuv
        if new_v_dist < dist[v]:
          dist[v] = new_v_dist
          parent[v] = current
          est_ttl[v] = new_v_dist + hrstc[v]
          if v not in fringe: fringe.append(v)

  print(msg)
  print('')

G = weight3.G9
print(G)
astar(G,'A','Z')
