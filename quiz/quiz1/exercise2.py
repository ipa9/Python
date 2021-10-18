x = input("Write the sentence: ")
a = ()
x = tuple(x.split(" "))
for word in x:
    if 'a' in word or 'b' in word:
        a = a + (word,)
print(a)
