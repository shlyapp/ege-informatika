for A in range(1, 100):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            if (((2*y+x)<A) or (x>10) or (y>25)) == 0:
                flag = False
                break
    if (flag):
        print(A)
        break