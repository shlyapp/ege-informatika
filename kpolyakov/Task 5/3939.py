def F(n):
    num = bin(n)[2:]
    if (num.rfind('0') != -1):
        n = num.rfind('0')
        num = num[0:n] + num[:2] + num[n+1:len(num)]
        return int(num[::-1], 2)
    else:
        return 0

maxi = 0
for i in range(1, 100000):
    if (F(i) == 119):
        maxi = max(maxi, i)

print(maxi)