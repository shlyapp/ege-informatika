import itertools

a = list(itertools.product('ВИНТ', repeat = 5))
print(*a[1018])