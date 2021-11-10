def F(n):
    if (n > 15):
        return n * n - 5
    return n * F(n + 2) + n + F(n + 3)

print(sum(map(int, str(F(1)))))
