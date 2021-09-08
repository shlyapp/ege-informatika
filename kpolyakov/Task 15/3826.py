for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if ((A%35==0) and ((730%x==0) <= ((A%x!=0) <= (110%x!=0)))) == 0:
            flag = False
            break
    if (flag):
        print(A)
        break