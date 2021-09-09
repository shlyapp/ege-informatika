for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if ((x&13==0) <= ((x&40!=0) <=(x&A!=0))) == 0:
            flag = False
            break
    if (flag):
        print(A)
        break