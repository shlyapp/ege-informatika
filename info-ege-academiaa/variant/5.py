def F(num):
    num = bin(num)[2:]
    while len(num) < 8:
        num = '0' + num
    num = num.replace('1', '#').replace('0', '1').replace('#', '0')
    return int(num, 2)

for i in range(1, 100000):
    if (F(i) - i == 113):
        print(i)
        break
