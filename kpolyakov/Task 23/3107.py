def F(start, end):
    if (start > end):
        return 0
    elif (start == end):
        return 1
    return F(start + 1, end) + F(start + 10, end)

print(F(11, 27))