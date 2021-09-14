import itertools

a = list(itertools.product('АКРУ', repeat = 5))

print(*a[349])