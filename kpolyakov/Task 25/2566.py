def search_divisors(num):
    divisors = set()
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num // i)
    return divisors

for i in range(251811, 251827):
    d = search_divisors(i)
    if len(d) == 4:
        print(*sorted(d)[2:])
