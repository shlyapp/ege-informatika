for i in range(174457, 174506):
    a = []
    for x in range(2, i // 2 + 1):
        if (i % x == 0):
            a.append(x)
            if len(a) > 2:
                break
    if len(a) == 2:
        print(*a)

