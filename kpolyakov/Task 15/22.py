for A in range(0, 1000000):
    flag = True
    for x in range(0, 1000000):
        if ((x&25!=0) <=((x&17==0) <= (x&A!=0))) == 0:
            flag = False
            break
    if (flag):
        print(A)
        break