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
