def howMany(aDict):
    counter = 0
    for e in aDict:
        counter += len(aDict[e])
    print (counter)
    return counter
    
animals = { 'a' : ['aardvark'], 'b':['baboon'], 'c':['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

howMany(animals)
