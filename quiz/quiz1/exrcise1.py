bin = int(input("Write binary numb: "))

decimal = 0
i = 1
while bin > 0:
    decimal = decimal + (bin % 10) * i
    bin = bin // 10
    i = i * 2
    
print(decimal)
