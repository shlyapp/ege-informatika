from tkinter import N


def F(num):
    n = bin(num)[2:]
    while len(n) < 8:
        n = '0' + n
    index = n[::-1].find('1')
    n = n[:index - 1].replace('0', '#').replace('1',
                                                '0').replace('#', '1') + n[index - 1:]
    return int(n, 2)


for i in range(257):
    if F(i) == 221:
        print(i)
