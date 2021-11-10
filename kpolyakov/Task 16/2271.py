def F(n):
    if (n > 3):
        if (n % 2 == 0): return 2*n + F(n-1)
        else: return n*n + F(n-2)
    else:
        return n

counter = 0
for i in range(1, 101):
    if (F(i) % 3 == 0):
        counter += 1

print(counter)