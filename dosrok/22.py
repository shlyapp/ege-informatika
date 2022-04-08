def F(s):
    P = 10
    Q = 8
    K1 = 0
    K2 = 0
    while s <= 100:
        s = s + P
        K1 = K1 + 1
    while s >= Q:
        s = s - Q
        K2 = K2 + 1
    K1 += s
    K2 += s
    return (K1, K2)

for s in range(10000):
    if F(s) == (10, 19):
        print(s)
        break