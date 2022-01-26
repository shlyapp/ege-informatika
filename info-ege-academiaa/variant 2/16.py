def F(n):
    if n > 1:
        return 3 * F(n - 1) + G(n - 1) - n + 5
    return 1

def G(n):
    if n > 1:
        return F(n - 1) + 3*G(n - 1) - 3*n
    return 1

print(F(14)+G(14))