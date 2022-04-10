def F(s):
    n = 0
    while 2*s*s <= 10*s:
        s = s + 1
        n = n + 2
    return n


for s in range(1, 10000):
    if F(s) == 8:
        print(s)
