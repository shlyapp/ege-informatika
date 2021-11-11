def F(n):
    if (n >= 10):
        return n % 10 + F(n // 10)
    return n

def G(n):
    if (n >= 10):
        return G(F(n))
    return n

counter = 0
for i in range(10, 100):
    counter += G(i)

print(counter)