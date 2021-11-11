from functools import lru_cache

@lru_cache

def F(n):
    if (n > 3):
        if (F(n-1) % 2 == 0): return F(n - 2) + n
        else: return F(n - 2) + 2 * n
    return n + 3

counter = 0
for i in range(40, 51):
    counter += F(i)

print(counter)