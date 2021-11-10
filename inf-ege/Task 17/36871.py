def F(n):
    if (n > 0 and n % 2 == 0):
        return F(n / 2)
    if (n % 2 != 0):
        return 1+ F(n - 1)
    return 0

counter = 0
for i in range(1, 1001):
    if (F(i) == 3):
        counter += 1

print(counter)