from email.policy import default


def div(x):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return sorted(d)

for x in range(1_500_001, 1_500_100):
    d = div(x)
    if len(d) > 0:
        sr = sum(d) // len(d)
        if sr % 10 == 9:
            print(x, sr)
