def F(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    return F(start + 2, end) + F(start * 2, end)

print(F(1, 16) * F(16, 52))