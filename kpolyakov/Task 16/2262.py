def F(n):
    if (n>=2):
        return F(n-1) - n*G(n-1)
    return 1

def G(n):
    if (n>=2):
        return F(n-1) + 2*G(n-1)
    return 1

print(G(18))