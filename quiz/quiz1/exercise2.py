#Write a function that takes a tuple where there are 15 words, the program should copy to another tuple only the words that contain the letters a and b

x = input("Write the sentence: ")
a = ()
x = tuple(x.split(" "))
for word in x:
    if 'a' in word or 'b' in word:
        a = a + (word,)
print(a)
