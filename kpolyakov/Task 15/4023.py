for A in range(1, 10000):
    flag = True
    for x in range(1, 10000):
        if ((x&87==0) <= ((x&31!=0) <=(x&A==0))):
            flag = False
    if (flag):
        print(A)
        break