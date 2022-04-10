def convert(num, base):
    answer = ''
    while num > 0:
        answer = str(num % base) + answer
        num = num // base
    return answer


num = 5**2004 - 5**1016 - 25**508 - 5**400 + 25**250 - 27

print(convert(num, 5).count('4'))
