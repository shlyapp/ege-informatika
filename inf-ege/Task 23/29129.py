def f(x, end):
    if x > end:
        return 0
    if x == end:
        return 1
    return f(x+1, end) + f(x*2, end)

print(f(3, 13)*f(13, 30)*f(30, 60))