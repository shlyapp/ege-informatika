def f(s):
    n = 105
    while n > s:
        s = s + 3
        n = n - 2
    return n

for i in range(-1000, 1000):
    if f(i) == 67:
        print(i)
        break

print(f(10))