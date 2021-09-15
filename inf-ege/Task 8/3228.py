import itertools

a = list(itertools.product('АОУ', repeat = 5))
for i in range(len(a)):
    s = ''.join(a[i])
    #print(a[i])
    if (s == 'УАУАУ'):
        print(i+1)