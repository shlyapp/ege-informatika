def F(n):
    num = bin(n)[2:]
    while len(num) < 8:
        num = '0' + num
    index_last = len(num) - num[::-1].find('1') - 1
    num2 = ''
    for i in range(len(num)):
        if (i < index_last):
            if (num[i] == '0'): num2 += '1'
            if (num[i] == '1'): num2 += '0'
        else:
            num2 += num[i]
    return int(num2, 2)

for i in range(0, 256):
    if (F(i) == 211):
       print(i)
