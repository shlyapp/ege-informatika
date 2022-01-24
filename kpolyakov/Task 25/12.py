def div(x):
    d = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)

for x in range(193_136, 193_223 + 1):
    if len(div(x)) == 6:
        print(*div(x))