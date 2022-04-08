def F(num):
    n = bin(num)[2:]
    if (num % 2 != 0):
        n = '1' + n + '01'
    else:
        n = n + '10'
    return int(n, 2)

for num in range(1, 10000):
    if F(num) > 516:
        print(num)
        break