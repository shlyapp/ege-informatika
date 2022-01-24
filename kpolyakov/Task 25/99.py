def div(x):
    d = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)

for x in range(333_555, 777_999 + 1):
    d = [i for i in div(x) if len(str(i)) == 2]
    if len(d) == 35:
        print(x, min(d), max(d))