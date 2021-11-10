def F(n):
    if (n > 20):
        return n*n*n + n
    else:
        if (n % 2 == 0): return 3*F(n+1) + F(n+3)
        else: return F(n+2) + 2*F(n+3)

counter = 0
for i in range(1, 1001):
    if (str(F(i)).count('1') == 0):
        counter += 1
print(counter)