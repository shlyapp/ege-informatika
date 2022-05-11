def F(x):
    L = 0
    M = 0
    while x > 0:
        L = L + 1
        M = M + (x % 10)
        x = x // 10
    return (L, M)


for i in range(1000):
    if F(i) == (3, 7):
        print(i)
        break
