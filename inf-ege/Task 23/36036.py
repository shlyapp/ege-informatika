def f(x, end):
    if x == end:
        return 1
    if x < end:
        return 0
    return f(x-2, end) + f(x-5, end)

print(f(23, 2))