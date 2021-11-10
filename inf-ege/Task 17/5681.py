def F(n):
    if (n > 2):
        return 2 * F(n - 1) + F(n - 2)
    return 2

print(F(5))