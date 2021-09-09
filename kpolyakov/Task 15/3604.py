for A in range(0, 1000):
    flag = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if (((5*x - 6*y) < A) or ((x-y)>30)) == 0:
                flag = False
                break
    if (flag):
        print(A)
        break