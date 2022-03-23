from functools import lru_cache


@lru_cache
def F(n):
    if n > 5:
        if n % 8 == 0:
            return n + F(n / 2 - 3)
        else:
            return n + F(n + 4)
    else:
        return n


for n in range(0, 100):
    try:
        num = F(n)
        print(n)
    except:
        pass
