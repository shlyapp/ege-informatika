def F(n):
    num = bin(n)[2:]
    while len(num) < 8:
        num = '0' + num
    num2 = num.replace('0', '#').replace('1', '0').replace('#', '1')
    return int(num2, 2) - int(num, 2)

for i in range(0, 255):
    if (F(i) == 133):
        print(i)