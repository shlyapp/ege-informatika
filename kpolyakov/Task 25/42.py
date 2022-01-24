def is_simple(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))

for x in range(4_202_865, 4_202_923 + 1):
    if is_simple(x):
        print(x)