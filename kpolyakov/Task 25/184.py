def div(x):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)

for x in range(300_000_001, 300_020_000):
    d = div(x)
    if len(d) >= 5:
        P = d[0] * d[1] * d[2] * d[3] * d[4]
        if P % 100 == 31 and P <= x:
            print(P, d[4])