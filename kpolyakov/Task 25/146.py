def is_simple(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))

for x in range(50_000_000, 50_500_001):
    if int(x**0.5)**2 == x and is_simple(int(x**0.5)):
        print(2 * int(x ** 0.5) ** 2, int(x ** 0.5) ** 2)