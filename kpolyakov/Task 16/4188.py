def F(n):
    if (0 < n <= 10):
        return F(n - 1)
    if (10 < n < 100):
        return 2.2 * F(n - 3)
    if (n >= 100):
        return 1.7 * F(n-2)
    return 1

print(sum(map(int, str(int(F(40))))))