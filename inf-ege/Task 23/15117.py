def F(start, end):
    if (start > end or start == 15):
        return 0
    elif (start == end):
        return 1
    return F(start + 1, end) + F(start + 2, end)

print(F(3, 9) * F(9, 20))