#3. Write a function that will print how many times 'hello' is repeated in the string. For example, if s = “hihellohellonohellon”, then the program should print 3. 
#Do not use count.

h = 0
s = 'hihellohellonohellon'
for i in range(1, len(s)-1):
    if s[i-1:i+4] == 'hello':
        h += 1
print ('Hello is repeated:', h,'times')
