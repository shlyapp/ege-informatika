for i in range(23, 35):
    a = []
    for x in range(1, i + 1):
        if (i % x == 0): 
            a.append(x)
    if (len(a) == 2):
        print(i**2, i**3)