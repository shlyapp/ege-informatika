def div(x):
    d = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)

for x in range(250_000, 250_200 + 1):
    d = [i for i in div(x) if i % 2 == 0]
    if len(d) == 6:
        print(d[-2], d[-1])