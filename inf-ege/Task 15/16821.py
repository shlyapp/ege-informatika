for A in range(0, 100):
    flag = True
    for x in range(0, 100):
        for y in range(0, 100):
            if not(((3*x + 4*y) != 70) or (A>x) or (A>y)):
                flag = False
                break
    if (flag):
        print(A)
        break