def F(n):
    num = bin(n)[2:]
    num2 = ''
    for letter in num:
        if (letter == '1'): num2 += '0'
        else: num2 += '1'
    return int(num2, 2)

for i in range(0, 256):
    if (F(i) == 98):
        print(i)