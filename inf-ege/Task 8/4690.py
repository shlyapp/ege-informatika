import itertools

a = list(itertools.product('.-', repeat = 3)) + list(itertools.product('.-', repeat = 4))
print(len(a))
