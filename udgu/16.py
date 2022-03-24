def F(n):
    if n > 5:
        if n % 3 == 0:
            return n + F(n / 3 + 2)
        else:
            return n + F(n + 3)
    else:
        return n


for n in range(0, 10000):
    try:
        print(n, F(n))
    except:
        pass
