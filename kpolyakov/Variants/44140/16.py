from functools import lru_cache


@lru_cache()
def F(n):
    if n < -100000:
        return 1
    elif n > 10:
        return F(n - 1) + 3 * F(n-3) + 2
    else:
        return -F(n - 1)


print(F(10))
