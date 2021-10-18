"""
Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print 2
"""

numBobs = 0
s = 'azcbobobegghakl'
for i in range(1, len(s)-1):
    if s[i-1:i+2] == 'bob':
        numBobs += 1
print ('Number of times bob occurs is:', numBobs)
