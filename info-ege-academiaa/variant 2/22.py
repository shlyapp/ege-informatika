def f(x):
    a = 0
    b = 0 
    while x > 0:
        a = a + 1 
        b = b + (x % 100)
        x = x // 100
    return (a, b)

counter = 0

for i in range(1, 4_000_000):
    if f(i) == (2, 12):
        counter += 1

print(counter)