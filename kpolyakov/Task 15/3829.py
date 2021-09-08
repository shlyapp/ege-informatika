counter = 0
for A in range(1, 1001):
    flag = True
    for x in range(1, 1001):
        if ((A%12==0) and ((530%x==0) <=((A%x!=0) <= (170%x!=0)))) == 0:
            flag = False
            break
    if (flag):
        counter += 1
print(counter)