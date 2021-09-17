import itertools

def f(x, y, A):
    return ((x in A) <= (x * x <= 81)) and ((y * y <= 36) <= (y in A))

A = set(range(-100, 100))
for x, y in itertools.product(range(-100, 100), repeat=2):
    if not f(x, y, A):
        A.remove(x)

print(*sorted(A))