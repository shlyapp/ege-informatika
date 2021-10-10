def F(n):
    x = n
    a, b = 0, 1
    while x > 0:
        a = a + 1
        b = b * (x % 10)
        x = x // 10
    return [a, b]

for i in range(1, 10000):
    if (F(i) == [4, 24]):
        print(i)
        break