import random, math

def compositeWitness(w,n,verbose): # miller rabin
  # is w witness for n composite ?
  assert 1==n%2
  s,z = 0, n-1
  while (0== z%2):
    s+=1
    z/=2
  y = pow(w,z,n)
  for j in range(s):
    z = (y*y)%n
    if z == 1 and y !=1 and y != n-1:
      if verbose: print w, 'yields root', y
      return True  # yes, composite
    y = z
  if (z != 1):
    if verbose: print w, '  fails Fermat'
    return True    # yes, composite
  return False       # no, probably prime

def isComposite(n,t,verbose): # t trials to show composite
  print '  seek composite witness:',
  if verbose: print n,
  knownComposite = False
  tries = 0
  while (not knownComposite) and (tries < t):
    tries += 1
    a = random.randint(2,n-2)
    knownComposite = compositeWitness(a,n,verbose)
    if verbose and not knownComposite: print a,
  return knownComposite

def primetest(n,t,verbose):
  if isComposite(n,t,verbose):
    print n,'composite'
  else:
    print n,'prime\nProb >= 1.0 -', pow(.25,t)

def primegen(n,t,verbose): # find n-bit probable-prime
  found = False
  low, high = pow(2,n-2), pow(2,n-1)-1
  attempts = 0
  while not found:
    attempts += 1
    a = 2*random.randint(low,high)+1
    if verbose: print a
    found = not isComposite(a,t,verbose)
  if verbose: print '\n', attempts, 'attempts before probable-prime found'
  return a, attempts  # Prob(a prime) >= 1 - (1/4)^t

#primetest(987613,1,True)

numbits, experiments, t, sum = 100, 10, 20, 0
for j in range(experiments):
  print 'experiment',j, ': find probable-prime, prob. >= 1.0 -', pow(.25,t), '\n'
  sum += primegen(numbits,t,True)[1]
print '\navg attempts to find prime', sum/(experiments*1.0)
print 'expected number of attempts', math.log(pow(2,numbits))/2.0
