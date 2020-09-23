#!/usr/local/bin/python3
'''
simple heap operations: bubbleup, trickledown, makeheap

* binary tree rooted at element k satisifes min-heap property iff
  - element less than or equal to its left  child (if it has a left  child) and
  - element less than or equal to its right child (if it has a right child)

* human indexing: (1st element has index 1) for S[j]
      parent:      S[ j // 2 ]  (integer floor of n over 2)
      left  child: S[ 2*j    ]
      right child: S[ 2*j+1  ]

* python indexing: (1st element has index 0) for S[j]
      parent:      S[ j-1 // 2 ]  (integer floor of n over 2)
      left  child: S[ 2*j + 1  ]
      right child: S[ 2*j + 2  ]
'''

import random  
from copy import deepcopy

def indices(n): # print indices
  print(' ', end=' ')
  for j in range(n): print('{:2}'.format(j), end=' ')
  print('')

def pretty(S): # print sequence
  print ('[', end=' ')
  for j in S: print('{:2}'.format(j), end=' ')
  print (']')

def genseq(n):
  S = []
  for j in range(n): 
    S.append(j)
  random.shuffle(S)
  return S

def swapvals(S,j,k):
  t = S[j]
  S[j] = S[k]
  S[k] = t

def bubbleup(S,j):
# if   S[0 .. j-1] satisifies heap property before execution, 
# then S[0 .. j  ] satisifies heap property after  "
# print('\nbubble from', j, end='')
  while j > 0:
    pj = (j-1)//2  # parent of j
    if S[pj] <= S[j]: break
    swapvals(S, j, pj)
    j = pj

def trickledown(S,j):
# for binary subtree T rooted at S[j], with left,right subtrees T_L, T_R
# if  both T_L, T_R satisfy    heap property before execution,
# then  T           satisifies heap property after  "
# print('\ntrickle from', j, end='')
  n = len(S)
  while True: 
    left, right = 2*j+1, 2*j+2
    if left >= n: break # because j has no children
    best = left         # best child so far
    if right < n and S[right] < S[left]:  # short-circuit evaluation :)
      best = right      # new best child
    if S[j] <= S[best]: break # heap property restored
    swapvals(S, j, best)
    j = best            # descend and repeat

def makeheap(S):
  for j in range(1,n):
    bubbleup(S,j)
    #print('bubbleup', j, 'done')
    #pretty(S)

def makeheap2(S):
  for j in range((n-1)//2, -1, -1): # python, count down from floor (n-1)/2 to 0
    trickledown(S,j)

n = 10
S = genseq(n)
#S = [5, 1, 3, 7, 8, 4, 9, 2, 6, 0]
T = deepcopy(S)
indices(n)
pretty(S)
pretty(T)
for count in range(2):
  if count % 2 == 0: 
    makeheap(S)
    pretty(S)
  else:              
    makeheap2(T)
    pretty(T)
