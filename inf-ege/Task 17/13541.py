def F(n):
    if (n > 2):
        return F(n - 1) + G(n - 2)
    return n

def G(n):
    if (n > 2):
        return G(n - 1) + F(n-2)
    return 3 - n

print(G(6))
