for A in range(0, 1000):
    flag = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if (((x*y)<100) or (y>=A) or (x>A)) == 0:
                flag = False
                break
    if (flag):
        print(A)