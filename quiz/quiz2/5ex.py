#5. Write a function that converts a binary number to decimal. If the number is not binary the function should throw an error. Do not use the ready conversion function.

def FromBinToDec(binNum):
    Binary = set(binNum)
    iferr = {'0', '1'}
    if Binary == iferr or Binary == {'0'} or Binary == {'1'}:
        binNum = int(binNum)
    else:
        return "Error!!!"

    decNum = 0
    Deg = 1
    while binNum > 0:
       decNum += (binNum % 10)*Deg
       binNum //= 10
       Deg = Deg*2
    return decNum

binNum = input("Enter binary number: ")

print("Decimal of", binNum, "is:", FromBinToDec(binNum))
