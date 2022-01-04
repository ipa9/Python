#   5.	You have an empty set; the program must fill this set with 50 random items. 
#   In this set we have to count the sum of the elements, also we have to copy the elements of this set into the tuple and into the list. 

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
