def F(x):
    L = 0
    M = 0
    while x > 0:
        L = L + 1
        if x % 2 == 1:
            M = M + (x % 10)
        x = x // 10
    return (L, M)

for x in range(1, 10000):
    if (F(x) == (3, 8)):
        print(x)
        break
