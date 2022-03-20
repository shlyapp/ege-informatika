def F(x, end):
    if (x == end):
        return 1
    if (x > end) or (x == 8):
        return 0
    return F(x + 2, end) + F(x * 3, end)


print(F(1, 49))
