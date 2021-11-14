def F(start, end):
    if (start > end or start == 26):
        return 0
    elif (start == end):
        return 1
    return F(start + 1, end) + F(start * 2 + 1, end)

print(F(1, 27))