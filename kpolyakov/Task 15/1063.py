for A in range(0, 100):
    flag = True
    for x in range(0, 100):
        for y in range(0, 100):
            if ((((3*x)+(2*y)) != 90) or ((A>x) and (A>y))) == 0:
                flag = False
                break
    if (flag):
        print(A)
        break