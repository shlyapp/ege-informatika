def F(n):
    if (n >= 2):
        if (n % 3 == 0): return F(n/3) - 1
        else: return F(n - 1) + 17
    return 1

counter = 0
for i in range(1, 100001):
    if (F(i) == 43):
        counter += 1

print(counter)
