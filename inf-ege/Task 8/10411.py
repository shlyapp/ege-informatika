import itertools

a = list(itertools.product('ABCX', repeat = 5))
counter = 0
for i in a:
    if (i.count('X') == 1):
        counter += 1
print(counter)
