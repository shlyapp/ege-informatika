from functools import lru_cache

@lru_cache

def F(n, m):
    if (m == 0):
        return n
    return F(m, n % m)

a = set()
for n in range(100, 1001):
    for m in range(100, 1001):
        print(n, m)
        try:
            if (F(n, m) == 30):
                a.add(n)
        except:
            continue

print(len(a))