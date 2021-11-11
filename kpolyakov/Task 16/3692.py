def F(n):
    if (n > 1):
        if (n % 3 == 0): return n + F(n / 3)
        else: return n + F(n + 3)
    return n

for i in range(1, 10000):
    try:
        if (F(i) > 100):
            print(i)
            break
    except:
        continue

