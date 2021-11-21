from itertools import product

a = list(product('ABCDEFGH', repeat = 4))

for i in range(len(a)):
    element = ''.join(a[i])
    if (element == 'DDFA'):
        print(i + 1)
        break