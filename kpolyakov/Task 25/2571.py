for i in range(190201, 190221):
    a = []
    for x in range(2, i//2+1):
        if (i % x == 0):
            a.append(x)
            if len(a) > 6:
                break
    if len(a) == 2:
        a.sort()
        print(i, a[1])