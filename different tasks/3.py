"""
SQUARE with WHILE
"""
x = int(input("Enter number you want to be squared: "))
ans = 0
itersLeft = x
while (itersLeft != 0):
    ans = ans + x
    itersLeft = itersLeft - 1
print(str(x) + ' * ' + str(x) + ' = ' + str(ans))
