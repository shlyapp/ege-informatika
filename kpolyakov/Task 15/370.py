k = 10000
for A in range(1, k + 1):
    z = True
    for x in range(1, k + 1):
        if ((x%A!=0) <= ((x%6==0) <= (x%4!=0))) == 0:
            z = False
            break
    if (z):
        print(A)
    else:
        k += 10000
