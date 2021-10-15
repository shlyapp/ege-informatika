def F(n):
    num = bin(n)
    num = num[2:]
    for i in range(1, len(num)):
        if (num[i]=='0'): num = num.replace('0', '1', 1)
        else: num = num.replace('1', '0', 1)
    num = int(num, 2)
    return n+num

for i in range(0, 1000):
    if F(i) > 123:
        print(i - 1)
        break
