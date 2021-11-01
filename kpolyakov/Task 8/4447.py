import itertools
from typing import Counter

a = set(list(itertools.permutations("МАРИНА", r = 6)))
counter = 0

for element in a:
    element = ''.join(element)
    if (element[0] != 'А' and element[0] != 'И'):
        counter += 1

print(counter)