k = 10000
for A in range(1, k + 1):
    z = True
    for x in range(1, k + 1):
        if ((A < 50) and ((x%A!=0) <= ((x%10==0) <= (x%18!=0)))) == 0:
            z = False
            break
    if (z):
        print(A)
