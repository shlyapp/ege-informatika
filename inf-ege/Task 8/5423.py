import itertools

a = list(itertools.product('ABC', repeat=2)) + list(itertools.product('ABC', repeat=3)) + list(itertools.product('ABC', repeat = 4))
print(len(a))