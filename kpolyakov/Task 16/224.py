def F(n):
    if (n>1):
        if (n%2==0):
            return n*n + F(n-1)
        else:
            return F(n-1) + 2*F(n-2)
    return 1
    
print(F(23))