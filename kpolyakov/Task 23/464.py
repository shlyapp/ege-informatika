def F(n, end):
    if n == end:
        return 1
    if n > end:
        return 0
    return F(n + 1, end) + F(n * 2, end)

print(F(1, 10) * F(10, 21))