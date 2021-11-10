def F(n):
    if n > 2:
        F(n - 2)
        print(n, end='')
        F(n // 2)

F(9)