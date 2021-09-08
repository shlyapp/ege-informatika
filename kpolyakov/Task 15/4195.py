for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if ((not((x%16==0) == (x%24==0))) <= (x%A==0)) == 0:
            flag = False
            break
    if (flag):
        print(A)