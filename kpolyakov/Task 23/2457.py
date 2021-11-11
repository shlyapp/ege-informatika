def F(x, end):
    if (x == end):
        return 1
    if (x > end) or (x == 8):
        return 0
    return F(x + 1, end) + F(x + 4, end) + F(x * 4, end)

print(F(2, 6) * F(6, 24))