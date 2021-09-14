import itertools

a = list(itertools.product('01234567', repeat = 4))
counter = 0

for x in a:
    if (x[0] != '0'):
        num = int("".join(list(map(str, x))))
        if (num%4==0):
            counter+=1

print(counter)