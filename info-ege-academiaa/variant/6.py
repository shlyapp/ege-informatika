def F(s):
    n = 1
    while s < 208:
        s += 20
        n *= 2
    return n

for s in range(1, 1000000):
    if (F(s) == 256):
        print(s)