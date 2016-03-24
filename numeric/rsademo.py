pA, qA = 3581, 3607
pB, qB = 3583, 3593
nA, nB = pA*qA, pB*qB
eA = 769
eB = 401
phinA = (pA-1)*(qA-1)
phinB = (pB-1)*(qB-1)

print nA, nB, eA, eB, phinA, phinB
dA, dB = 3122449, 5101697
assert((dA*eA)%phinA ==1)
assert((dB*eB)%phinB ==1)
M = [19361, 4964, 1641]
sig = pow(6675,dA,nA)
M.append(sig)
print M
toB = []
for m in M:
  toB.append(pow(m, eB, nB))
print toB
msg = []
for b in toB:
  msg.append(pow(b, dB, nB))
print msg

print pow(msg[3],eA,nA)
