import itertools

a = list(itertools.product('АОУ', repeat=5))

for i in range(len(a)):
    print(i + 1, a[i])
