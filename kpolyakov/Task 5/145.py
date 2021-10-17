def F(n):
    num = list(map(int, str(n)))
    a = num[0]*num[1]
    b = num[1]*num[2]
    if (a>b):
        return str(b)+str(a)
    else:
        return str(a)+str(b)

for i in range(100, 1000):
    if (F(i) == '621'):
        print(i)