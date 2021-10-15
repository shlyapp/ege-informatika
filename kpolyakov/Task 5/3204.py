def F(n):
    num = bin(n)[2:]
    num = num + num[-2]
    num = num + num[1]
    return int(num, 2)

for i in range(11, 1000):
    if F(i) > 170:
        print(i)
        break