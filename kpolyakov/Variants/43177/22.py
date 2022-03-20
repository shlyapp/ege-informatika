def F(x):
    a = 0
    b = 1
    while x > 0:
        a = a + 1
        b = b*(x % 10)
        x = x//10
    return (a, b)


counter = 0
for x in range(1, 100000):
    if F(x) == (2, 24):
        counter += 1

print(counter)
