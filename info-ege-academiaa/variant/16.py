from functools import lru_cache

@lru_cache

def F(n):
    if (n > 13):
        if (n % 3 == 0): return F(n - 1) + 2 * n ** 2 - 3
        else: return F(n - 2) + 3 * n + 6
    return n ** 3 + n ** 2 + 1

counter = 0

for i in range(1, 1001):
    num = F(i)
    if (sum(list(map(lambda x: int(x) % 2, str(num))))) == len(str(num)):
        print(F(i))
        counter += 1

print(counter)

