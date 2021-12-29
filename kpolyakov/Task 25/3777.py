for i in range(1, 1000):
    divisors = []
    for x in range(1, i + 1):
        if i % x == 0:
            divisors.append(x)
    if (sum(list(map(lambda x: x % 2, divisors))) == 5):
        print(i)
        
