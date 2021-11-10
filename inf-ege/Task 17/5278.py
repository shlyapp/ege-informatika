def F(n):
    if (n > 1):
        return 2*F(n-1)+1
    return 1

print(F(5))