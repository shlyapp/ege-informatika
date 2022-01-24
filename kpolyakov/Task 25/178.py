def div(x):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)

for x in range(500_001, 500_100):
    d = [i for i in div(x) if i % 10 == 8 and i != 8]
    if len(d) > 0:
        print(x, d[0])