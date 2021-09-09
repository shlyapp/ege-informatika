for A in range(0, 1000):
    flag = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if ((x&77!=0) <= ((x&12==0) <= (x&A!=0))) == 0:
                flag = False
                break
    if (flag):
        print(A)
        break