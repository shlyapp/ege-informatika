import itertools

a = list(itertools.product('ABCDE', repeat=3))
print(len(a))