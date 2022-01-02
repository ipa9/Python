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
