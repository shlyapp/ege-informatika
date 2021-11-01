import itertools
from typing import Counter

a = list(itertools.product('01234567', repeat = 4))
counter  = 0

for element in a:
    element = ''.join(element)
    if (element[0] != '0' and int(element[0]) % 2 == 0):
        if (ord(element[0]) >= ord(element[1]) >= ord(element[2]) >= (ord(element[3]))):
            counter += 1

print(counter)