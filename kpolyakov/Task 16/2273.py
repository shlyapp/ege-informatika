def F(n):
    if (n > 1):
        if (n % 2 == 0): return n * F(n-1)
        else: return n + F(n-2)
    return 1

print(F(84))