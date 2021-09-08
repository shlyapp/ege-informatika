for A in range(1, 100):
    flag = True
    for x in range(1, 100):
        if ((((x%12==0) or (x%36==0)) <= (x%A==0)) and ((A**2-A-90) < 0)) == 0:
            flag = False
            break
    if (flag):
        print(A)
    