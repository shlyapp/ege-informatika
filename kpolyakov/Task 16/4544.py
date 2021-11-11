from functools import lru_cache

@lru_cache

def F(n):
    if (n > 0):
        if (n % 2 == 0): return F(n / 2) - 1
        else: return 3 + F(n - 1)
    return 0

a = set()
i = 999
while i != 0:
    a.add(F(i))
    i -= 1

print(len(a))

    