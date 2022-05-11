def F(s):
    n = 1
    while s < 185:
        s = s + 30
        n = n * 3
    return n


for i in range(100000):
    if F(i) == 729:
        print(i)
