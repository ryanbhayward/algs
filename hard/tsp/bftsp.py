"""
    Author: Simon Westphahl <westphahl@gmail.com>
    Description: Brute-force implementation for solving the TSP.
    http://en.wikipedia.org/wiki/Travelling_salesman_problem
"""

# modified rbh 2022: read inter-city distances from stdin
from sys import stdin
from init_dists import init_distance_dict

routes = []

def find_paths(node, cities, path, distance):
    # Add way point
    path.append(node)

    # Calculate path length from current to last node
    if len(path) > 1:
        distance += cities[path[-2]][node]

    # If path contains all cities and is not a dead end,
    # add path from last to first city and return.
    if (len(cities) == len(path)) and (path[0] in cities[path[-1]]):
        global routes
        path.append(path[0])
        distance += cities[path[-2]][path[0]]
        #print (path, distance)
        routes.append([distance, path])
        return

    # Fork paths for all possible cities not yet used
    for city in cities:
        if (city not in path) and (node in cities[city]):
            find_paths(city, dict(cities), list(path), distance)

def tri_eq(a,b,c):
  return (a+b >= c) and (b+c >= a) and (c+a >= b)

def tri_eq_check(D):
  if len(D) < 3:
    return True
  towns = []
  for j in D:
    towns.append(j)
  print(towns)
  n = len(towns)
  for j in range(n-2):
    for k in range(j+1, n-1):
      for m in range(k+1, n):
        if not tri_eq(D[towns[j]][towns[k]], 
                      D[towns[j]][towns[m]], 
                      D[towns[k]][towns[m]]):
          print('triangle equality violation')
          print(towns[j], towns[k], towns[m], 
                D[towns[j]][towns[k]], 
                D[towns[j]][towns[m]], 
                D[towns[k]][towns[m]])
          assert(False)
  print('triangle inequality ok')

if __name__ == '__main__':
    cities = {
        'A': {'B':45, 'C':25, 'D':38, 'E':30, 'F':50, 'G':67, 'H':61, 'I':85, 'J':77},
        'B': {        'C':63, 'D':21, 'E':42, 'F':61, 'G':50, 'H':84, 'I':101,'J':79},
        'C': {                'D':49, 'E':29, 'F':39, 'G':67, 'H':40, 'I':65, 'J':65},
        'D': {                        'E':22, 'F':39, 'G':32, 'H':63, 'I':79, 'J':57},
        'E': {                                'F':22, 'G':38, 'H':42, 'I':61, 'J':47},
        'F': { 'G': 6, 'H': 7, 'I': 8, 'J': 9},
        'G': { 'H': 7, 'I': 8, 'J': 9},
        'H': { 'I': 8, 'J': 9},
        'I': { 'J': 9},
        'J': { 'K': 9},
        'K': { }, 
    }

    cities = init_distance_dict(False)  #not verbose
    tri_eq_check(cities)
    print ("Start: A")
    find_paths('A', cities, [], 0)
    print ("\n")
    routes.sort()
    if len(routes) != 0:
        print ("Shortest route: %s" % routes[0])
    else:
        print ("FAIL!")
