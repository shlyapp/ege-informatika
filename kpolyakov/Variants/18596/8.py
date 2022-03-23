import itertools
from xml.etree.ElementTree import iterparse

nums = list(itertools.permutations('0123456789ABCDEF', r=3))
forbiddens = list(itertools.permutations('02468ACE', r=2)) + \
    list(itertools.permutations('13579BDF', r=2))

counter = 0

for num in nums:
    num = ''.join(num)
    if (num[0] != '0'):
        for forbidden in forbiddens:
            forbidden = ''.join(forbidden)
            if forbidden in num:
                break
        else:
            counter += 1

print(counter)
