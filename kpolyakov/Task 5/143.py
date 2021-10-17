def F(n):
    num = list(map(int, str(n)))
    a = num[0]+num[2]+num[4]
    b = num[1]+num[3]
    if (a>b):
        return str(b)+str(a)
    return str(a)+str(b)

for i in range(10000, 100000):
    if (F(i) == '723'):
        print(i)
        break