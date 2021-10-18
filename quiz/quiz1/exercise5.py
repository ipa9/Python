numb = int(input("Enter Number from 0 to 2: "))
a = int(input("Enter any number: "))

def factorial (c):
    global b
    if c == 1:
        return 1
    return c * factorial(c-1)
b = 1
if numb == 2:
    print("Factorial: ", factorial(a))

elif numb == 1:
    i = 1
    while i <= a:
        b = b * i
        i = i + 1
    print("Factorial: ", b)
elif numb == 0:
    for i in range(1, a+1):
        b = b * i
    print("Factorial: ", b)
