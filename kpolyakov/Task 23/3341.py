def F(start, end):
    if (start > end or start == 15 or start == 8):
        return 0
    elif (start == end):
        return 1
    return F(start + 1, end) + F(start + 2, end) + F(start * 3, end)

print(F(3, 10)*F(10, 22))