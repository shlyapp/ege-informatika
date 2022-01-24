def div(x):
    d = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)

for x in range(244_143, 367_821 + 1):
    d = div(x)
    if len(d) == 5:
        print(d[-2], d[-1])