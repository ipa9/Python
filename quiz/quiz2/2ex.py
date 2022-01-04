#2. We have the following dictionary {'a': [], 'b': [], 'c': [], 'd': []}, the program must add one random number to a, one random number to b,
#then 4 random numbers to c and 7 random numbers to d, this must be done automatically in one for, write a function that returns: the key , 
#which contains the most elements, and also the product of all the values.

import random

key = ['a', 'b', 'c', 'd']
i, j = 1, 100
answer = dict()

for element in key:
    if element == 'a':
        answer[element] = random.sample(range(1, 100), 1)
    elif element == 'b':
        answer[element] = random.sample(range(1, 100), 1)
    elif element == 'c':
        answer[element] = random.sample(range(1, 100), 4)
    elif element == 'd':
        answer[element] = random.sample(range(1, 100), 7)

def maxNum(dictionary):
    maxElements = 0
    maxValue = 0
    maxKey = 0
    maxMultiplicated = 1
    for key, value in dictionary.items():
        if maxValue < len(value):
            maxKey = key
            maxValue = len(value)
            maxElements = value
    for element in maxElements:
        maxMultiplicated = maxMultiplicated*element

    return maxKey, maxMultiplicated

print(maxNum(answer))
