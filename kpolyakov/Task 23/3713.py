def F(start,  end):
    if (int(start, 2) > int(end, 2)):
        return 0
    elif (start == end):
        return 1
    return F(bin(int(start, 2) + 1)[2:], end) + F('1' + start, end)

print(F('100', '110001'))