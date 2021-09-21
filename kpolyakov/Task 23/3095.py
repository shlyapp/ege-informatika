def f(x, end):
    if x > end:
        return 0
    if x == end:
        return 1
    return f(x+1, end) + f(x*2, end) + f(2*x+1, end) + f(x*10, end)

print(f(1, 15))