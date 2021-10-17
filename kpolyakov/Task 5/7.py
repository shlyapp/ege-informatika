def F(n):
    num = bin(n)[2:]
    for i in range(2):
        num += str(sum(map(int, num))%2)
    return int(num, 2)

for i in range(1, 1000):
    if (F(i)>125):
        print(i)
        break