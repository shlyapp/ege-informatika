def is_simple(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))

def div(num):
    d = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    return sorted(d)

for x in range(650_001, 650_300):
    d = [i for i in div(x) if is_simple(i)]
    if sum(d) % 100 == 25:
        print(x, sum(d))
    