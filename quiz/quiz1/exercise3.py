import random

evenElem = ()
oddElem = ()
divbythree = ()

def randTuple():
    global evenElem, oddElem, divbythree
    for i in numbs:
        if i % 2 == 0:
            evenElem = evenElem + (i,)
        if i % 2 == 1:
            oddElem = oddElem + (i,)
        if i % 3 == 0:
            divbythree = divbythree + (i,)      
numbs = tuple(round(random.random()*100) for i in range(100))

randTuple()
print("Even numbers:",evenElem)
print("\nOdd numbers:", oddElem)
print("\nThree divider:", divbythree)
