h = 0
s = 'hihellohellonohellon'
for i in range(1, len(s)-1):
    if s[i-1:i+4] == 'hello':
        h += 1
print ('Hello is repeated:', h,'times')