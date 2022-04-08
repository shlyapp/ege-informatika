def F(s):
    s = (s - 10) // 7
    n = 1
    while s > 0:
        n = n * 2
        s = s - n
    return n

for s in range(0, 10000):
    if F(s) == 8:
        print(s)
        break