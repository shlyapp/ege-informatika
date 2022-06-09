def convert(num, base):
    n = ''
    while num > 0:
        n = str(num % base) + n
        num //= base
    return n


num = 27**45 + 9**70 - 3**10
print(convert(num, 3).count('0'))
