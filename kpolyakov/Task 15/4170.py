counter = 0
for A in range(1, 100000):
    flag = True
    for x in range(1, 100000):
        if ((A%5==0) and ((2020%A!=0) <= ((x%1718==0) <= (2023%A==0))))==0:
            flag = False
            break
    if (flag):
        counter+=1
print(counter)