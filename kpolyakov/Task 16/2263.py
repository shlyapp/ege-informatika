from functools import lru_cache

@lru_cache

def F(n):
    if (n >= 2):
        return F(n-1) - 2*G(n-1)
    return 1

def G(n):
    if (n >= 2):
        return F(n-1) + G(n-1) + n
    return 1

print(sum(map(int, str(G(36)))))
