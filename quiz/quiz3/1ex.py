#1.	The program asks us to enter the number of rows. The program should display the rows on the screen as follows (example of entering the number 6 is shown):
#    B
#    BC
#    BCD
#    BCDE
#    BCDEF
#    BCDEFG

n = int(input("Enter the number: "))
for i in range(n):
    for j in range(i+1):
        print(chr(j + 66), end = " ")
    print()
