def F(n):
    num = list(map(int, str(n)))
    num.sort()
    if (0 not in num):
        max = int(str(num[2]) + str(num[1]))
        min = int(str(num[0]) + str(num[1]))
        return max - min

counter = 0
for i in range(500, 601):
    if (F(i) == 10):
        counter += 1

print(counter)