def prime_deviders_fact(num):
    prime_deviders = []
    devider = 2

    while num > 1:
        while num % devider == 0:
            prime_deviders.append(devider)
            num /= devider
        devider += 1

    return prime_deviders

def find_prime_devider(num):
    prime_deviders = [2]
    counter = 3

    while len(prime_deviders) < num:
        dividers = []
        for element in prime_deviders:
            if (counter % element == 0):
                dividers.append(1)
            else:
                dividers.append(0)

        if (sum(dividers)) == 0:
            prime_deviders.append(counter)
        counter += 1

    return prime_deviders

def find_number(num):
    factorization_num = prime_deviders_fact(num)[::-1]
    print(f"factorization: {factorization_num}")
    primes_deviders = find_prime_devider(len(factorization_num))
    print(f"primes: {primes_deviders}")

    answer = 1
    for i in range(len(factorization_num)):
        answer *= primes_deviders[i]**(factorization_num[i]-1)

    first_prime = factorization_num[0]
    last_prime = primes_deviders[-1]

    while 2**(2*first_prime) < last_prime**2:
        answer = answer // last_prime**2 * 2**(2*first_prime)
        first_prime *= 2
        del primes_deviders[-1]
        last_prime = primes_deviders[-1]

    return (answer, primes_deviders[-1])

print(*find_number(729))


