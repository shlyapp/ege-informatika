def F(n):
    num = bin(n)[2:]
    if (num.count('1')>num.count('0')):
        num += '1'
    elif (num.count('1') == num.count('0')):
        num += '0'
    return int(num, 2)

for i in range(0, 10000):
    if (F(i) < 100):
        print(i)
