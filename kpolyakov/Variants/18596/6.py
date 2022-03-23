def F(s):
    n = 6
    while s <= 154:
        s = s + 12
        n = n + 3
    return n


for s in range(-10000, 10000):
    if F(s) == 42:
        print(s)
