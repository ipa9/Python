import random

Rset = set()
Rtuple = ()
Rlist = []

while len(Rset) < 50:
    Rset.add(random.randrange(0, 6535))

print (sum(Rset))

Rtuple = tuple(Rset)
Rlist = list(Rset)

print(Rset)
print(Rtuple)
print(Rlist)
