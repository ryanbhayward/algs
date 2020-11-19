#!/usr/local/bin/python3
# assume one line of input per node
# each line of input is
#   nodename node-x-coord node-y-coord
# e.g.
#  A  13 24
#  B  -6 11
from sys import stdin

def read_lcns():
  Lines = []
  for line in stdin:
    node = line.strip()
    Lines.append(node)
  return Lines

L = read_lcns()
for x in L:
  parts = x.split()
  print(parts[0], int(parts[1]), int(parts[2]))
