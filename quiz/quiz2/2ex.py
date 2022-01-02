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