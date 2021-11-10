def F(n):
    if (n > 5):
        if (n % 2 == 0): return F(n // 2) + n * n * n - 1
        else: return F(n - 1) + 2 * n * n + 1
    return n + 15

counter = 0
for i in range(1, 1001):
    if (str(F(i)).count('8') >= 2):
        counter += 1

print(counter)