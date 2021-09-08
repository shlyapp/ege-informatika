k = 100000

for A in range(1, k):
    z = True
    for x in range(1, k):
        if ((x%A==0) <= ((x%A==0) <= ((x%34==0) and (x%51==0)))) == 0:
            z = False
            break
    if (z):
        print(A)
        break
