def F(d):
    n = 8
    s = 78
    while s <= 1200:
        s = s + d
        n = n + 2
    return n


for d in range(1, 1000000):
    if F(d) == 46:
        print(d)
