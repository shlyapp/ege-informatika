def F(n, base):
    ans = ''
    while n > 0:
        ans = str(n % base) + ans
        n = n // base
    return ans


for i in range(2, 20):
    n = (F(381, i))
    if len(n) == 3 and n[-1] == '3':
        print(i)
