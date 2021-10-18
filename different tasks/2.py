"""
Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print Longest substring in alphabetical order is: beggh
"""

s = 'azcbobobegghakl'
test = s[0] 
best = ''
for n in range(1, len(s)):    
    if len(test) > len(best):
        best = test
    if s[n] >= s[n-1]:
        test = test + s[n]
    else:                     
        test = s[n]

print ("Longest substring in alphabetical order is:", best)
