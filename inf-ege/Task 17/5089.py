def F(n):
    if (n > 2):
        return 5 * F(n-1) - 4 * F(n - 2)
    return 5

print(F(13))