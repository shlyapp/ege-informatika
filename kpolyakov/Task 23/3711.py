def F(start, end):
    if (int(start, 2) < int(end, 2)):
        return 0
    elif (start == end):
        return 1
    return F(bin(int(start, 2) - 1)[2:], end) + F(start[:len(start) - 1], end)

print(F('100001', '100'))
