def F(start, end):
    if (start > end):
        return 0
    elif (start == end):
        return 1
    return F(start + 1, end) + F(int(''.join(str(x) for x in map(lambda x: int(x) + 1, str(start).replace('9', '8')))), end)

def upper_num(num):
    num = str(num).replace('9', '8')
    num2 = ''
    for element in num:
        num2 += str(int(element) + 1)
    return int(num2)

def F1(start, end):
    if (start > end):
        return 0
    elif (start == end):
        return 1
    return F1(start + 1, end) + F1(upper_num(start), end)

print(F1(25, 51))