#   6.	 We have an empty tuple that the program has to fill with 100 random elements, then the program has to move the even elements in one tuple,
#   the odd elements in the second tuple, and the elements in the tuple slide that are divisible by 3.
#   Save the received tuples to a file. The program must be done using the function.

import random

Rtuple = ()
oddtuple = ()
eventuple = ()
threetuple = ()

while len(Rtuple) < 100:
    Rtuple = Rtuple + (random.randrange(0, 6535),)

for i in Rtuple:

    if i % 2 == 1:
        oddtuple = oddtuple + (i,)

    if i % 2 == 0:
        eventuple = eventuple + (i,)

    if i % 3 == 0:
        threetuple = threetuple + (i,)

print(Rtuple)
print(oddtuple)
print(eventuple)
print(threetuple)
