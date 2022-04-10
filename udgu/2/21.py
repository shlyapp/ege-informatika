def F(start, end):
    if start < end:
        return 0
    if start == end:
        return 1
    if start > 4:
        return F(start - 1, end) + F(start - 3, end) + F(start % 4, end)
    else:
        return F(start - 1, end) + F(start - 3, end)


print(F(22, 2))
