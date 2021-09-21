def f(x, end):
    if x > end:
        return 0
    if x == end:
        return 1
    if x == 21:
        return 0
    return f(x+1, end) + f(2*x+1, end)

print(f(1, 25))