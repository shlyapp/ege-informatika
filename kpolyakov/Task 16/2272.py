def F(n):
    if (n > 3):
        if (n % 2 == 0): return n + 3 +F(n-1)
        else: return n*n + F(n-2)
    return n

counter = 0
for i in range(1, 1001):
    if (F(i) % 7 == 0):
        counter += 1

print(counter)