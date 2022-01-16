def F(n):
    if n > 15:
        if n % 2 == 0:
            return F(n // 2) + n * n * n - 5 * n
        else:
            return F(n - 1) + 2 * n + 3
    return n*n + 11

counter = 0
for n in range(1, 1001):
    if str(F(n)).count('6') >= 3:
        counter += 1

print(counter)
