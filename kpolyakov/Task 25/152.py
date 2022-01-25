def is_simple(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))

for x in range(63_000_000, 75_000_000 + 1):
    temp = x
    while temp % 2 == 0:
        temp //= 2
    if int(temp**0.25)**4 == temp and is_simple(int(temp**0.25)):
        print(x, temp)