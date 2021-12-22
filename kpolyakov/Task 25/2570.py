for i in range(135743, 135790):
    a = []
    for x in range(2, i//2+1):
        if (i % x == 0):
            a.append(x)
            if len(a) > 6:
                break
    if len(a) == 4:
        a.sort()
        print(a[3], i)

