for A in range(1, 100):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            if (((((x-20)<A) and ((10-y)<A))) or (((x+4)*y) > 45)) == 0:
                flag = False
                break
    if (flag):
        print(A)
        break