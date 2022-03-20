def F(n):
    if n < 6:
        return n + F(n+3)*F(2*n)
    else:
        return 2*n


print(F(3))
