import itertools

a = list(itertools.product('КОТ', repeat = 3))

for i in range(len(a)):
    element = ''.join(a[i])
    print(i + 1, element)