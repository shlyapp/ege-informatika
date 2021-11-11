def F(n):
    if (n > 0):
        if (n % 2 == 0): return F(n - 1) + F(n - 2)
        else: return 1.5 * F(n - 1)
    return 1

print(len(set(map(int, str(int(F(15)))))))