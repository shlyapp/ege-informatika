def search_divisors(num):
    divisors = set()
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num // i)
    return divisors

def is_super(num):
    div1 = search_divisors(num)
    div2 = search_divisors(sum(div1))
    return sum(div2) == num*2

maximum = 0
counter = 0

for x in range(2, 263001):
    if is_super(x):
        counter += 1
        maximum = max(maximum, x)

print(counter, maximum)

