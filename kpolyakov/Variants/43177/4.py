def F(n):
    num = bin(n)[2:]
    num = num[0] + \
        num[1:].replace('0', '#').replace('1', '0').replace('#', '1')
    num = int(num, 2)
    return n + num


for n in range(1, 1000):
    if n % 2 != 0 and F(n) > 99:
        print(n)
        break
