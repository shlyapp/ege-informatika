def func(s):
    n = 4
    while s < 37:
        s += 3
        n *= 2
    return n

for s in range(-1000, 1000):
    if func(s) == 128:
        print(s)
        break
