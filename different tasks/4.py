"""
CUBE root with WHILE
"""
x = int(input('Enter an integer: '))
ans = 0
while ans**3 < x:
    ans = ans + 1
if ans**3 != x:
    print(str(x) + ' is not perfect cube')
else:
    print('Cube root of ' + str(x) + ' is ' + str(ans))

    
    
#CUBE with FOR
cube = int(input("Enter CUBE: "))
for guess in range(cube+1):
    if guess**3 == cube:
        print("Cube root of", cube, "is", guess)
