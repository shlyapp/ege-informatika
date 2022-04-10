def F(n):
    if n >= 2:
        if n % 3 == 0:
            return F(n/3) - 1
        else:
            return F(n-1)+17
    return 1


for n in range(100000):
    if F(n) == 110:
        print(n)
        break
