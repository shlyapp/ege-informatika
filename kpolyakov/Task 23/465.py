def F(x, end):
    if x > end:
        return 0
    if x == end:
        return 1
    return F(x + 1, end) + F(x + 2, end)

print(F(3, 14) + F(3, 15))