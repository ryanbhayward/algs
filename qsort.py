# partition, qs:http://hetland.org/coding/python/quicksort.html
def partition(list, start, end):
  pivot = list[end]    # partition around the last value
  bottom = start-1     # initially outside sublist to be partitioned
  top = end            # "         "
  done = 0
  while not done:      # until all elements partitioned...
    while not done:  # until we find an out of place element...
      bottom = bottom+1  # move the bottom up.
      if bottom == top:  # if hit top...
        done = 1       # ... we are done.
        break
      if list[bottom] > pivot:     # bottom out of place?
        list[top] = list[bottom] # put it at top...
        break                    # ... resume search from top
    while not done:        # until we find an out of place element...
      top = top-1        # move top down.
      if top == bottom:  # if hit bottom...
        done = 1       # ... we are done.
        break
      if list[top] < pivot:        # top out of place?
        list[bottom] = list[top] # put it at bottom...
        break                    # ... resume search from bottom
  list[top] = pivot                    # replace pivot
  return top                           # return split index

def quicksort(list, start, end):
  if start < end:        # two or more elements?
    split = partition(list, start, end)
    quicksort(list, start, split-1)
    quicksort(list, split+1, end)
