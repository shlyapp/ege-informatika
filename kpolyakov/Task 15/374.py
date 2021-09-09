for A in range(1, 10000):
    flag = True
    for x in range(1, 10000):
        if ((x&A!=0) <= ((x&20==0) <= (x&5!=0))) == 0:
            flag = False
            break
    if (flag):
        print(A)