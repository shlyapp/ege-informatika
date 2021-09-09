for A in range(1, 1000000):
    flag = True
    for x in range(1, 1000000):
        if ((x&A!=0) <= ((x&14==0) <= (x&75!=0))) == 0:
            flag = False
            break
    if (flag):
        print(A)
    