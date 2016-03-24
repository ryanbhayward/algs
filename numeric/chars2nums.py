# convert character string to numeric string
# e.g., for using a PKC system
import sys
alphabet = 'abcdefghijklmnopqrstuvwxyz .?!,'
base = 1+len(alphabet)  #chars encrypted as 1 2 3 ...

def char2num(c): return 1+alphabet.find(c)
def num2char(x): return alphabet[x-1]
def myhash(L,modulus):
  s = ''
  for n in L: s += num2char((n*n)%modulus)
  return s

#convert string chars in list of at-most-d base-digit numbers
def encode(chars,digits):
  L = []
  for j in range(len(chars)):
    #print j, digits, j%digits, digits-1
    if j%digits == 0: n = 0
    n = n*base+char2num(chars[j])
    if (j%digits) == (digits-1) or (j == len(chars)-1): 
      L.append(n+1) # want smallest output number 2
  return L

def decode(L):
  s = ''
  for n in L:
    n -= 1  # remove extra from encode
    t = ''
    while (n>0):
      x,n = n%base, n/base
      t += num2char(x)
    # append in reverse order
    for j in reversed(range(len(t))):
      s += t[j]
  return s
  
charsPerWord = int(sys.stdin.readline().strip())
msg = sys.stdin.readline().strip('\n')
print charsPerWord, base, msg
#for c in msg:
  #x = char2num(c)
  #print x, num2char(x)
L= encode(msg,charsPerWord)
print L
print decode(L)
print myhash(L,23)
