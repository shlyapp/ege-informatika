def F(n):
    if (n > 0):
        return n % 10 * F(n // 10)
    return 1

for i in range(0, 1000):
    if (F(i) > 320):
        print(i, F(i))
        break