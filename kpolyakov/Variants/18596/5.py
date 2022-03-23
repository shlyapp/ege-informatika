def F(num):
    n = bin(num)[2:]

    while len(n) < 8:
        n = '0' + n

    index = len(n) - n[::-1].find('1')
    n = n[:index-1].replace('1', '#').replace(
        '0', '1').replace('#', '0') + n[index-1:]

    return int(n, 2)


for num in range(0, 1000):
    if F(num) == 98:
        print(num)
        break
