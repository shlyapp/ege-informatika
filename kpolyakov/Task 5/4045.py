def F(n):
    if (n % 2 == 0): n /= 2
    else: n -= 1

    if (n % 5 == 0): n /= 5
    else: n -= 5

    if (n % 7 == 0): n /= 7
    else: n -= 1

    return n

counter = 0

for i in range(1, 1000000):
    if (F(i) == 6):
        counter += 1

print(counter)