def F(n):
    num = bin(n)[2:]
    for i in range(2):
        num += str(sum(map(int, num))%2)
    return int(num, 2)

counter = 0
for i in range(1, 10000):
    if (210 <= F(i) <= 260):
        counter += 1

print(counter)