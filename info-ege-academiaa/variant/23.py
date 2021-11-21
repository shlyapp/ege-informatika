def F(start, end):
    if (start < end or start == 23):
        return 0
    elif (start == end):
        return 1
    return F(start - 2, end) + F(start - 3, end) + F(start // 2, end)

print(F(50, 30) * F(30, 18))