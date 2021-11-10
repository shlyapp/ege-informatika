from functools import lru_cache

@lru_cache

def F(n):
    if (n > 3):
        if (n % 2 == 0): return F(n - 1) + 2*F(n / 2)
        else: return F(n-1) + F(n-3)
    return n

counter = 0
for i in range(1, 10000):
    if (F(i) < 10**8):
        counter += 1
    else:
        print(F(i))
        break

print(counter)