for A in range(1, 100):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            if (((x**2 - 11*x + 28) > 0) or ((y**2 - 9*y + 14)>0) or ((x**2+y**2)>A)) == 0:
                flag = False
                break
    if (flag):
        print(A)