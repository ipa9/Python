#Newton-Raphson
#Generating guesses

eplision = 0.01
y = 24.0
guess = y/2.0
numGuesses = 0

while abs(guess*guess - y) >= eplision:
    numGuesses += 1
    guess = guess - (((guess**2) - y)/(2*guess))
print('numGuesses = ' + str(y) + ' is about ' + str(guess))
