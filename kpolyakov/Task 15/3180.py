for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if ((70%A==0) and ((x%A!=0) <= ((x%35==0) <= (x%63!=0)))) == 0:
            flag = False
            break
    if (flag):
        print(A)