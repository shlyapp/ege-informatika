from math import ceil, sqrt
for i in range(ceil(sqrt(51500000)), ceil(sqrt(52000000))):
    counter = 0
    for x in range(1, i + 1):
        if (i % x == 0):
            counter += 1
    if (counter == 2):
        print(i**2*2, i)





    
