for A in range(1, 100):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            if (((x*y)<(3*A)) or (x>=31) or (x<(5*y))) == 0:
                flag = False
                break
    if (flag):
        print(A)
        break