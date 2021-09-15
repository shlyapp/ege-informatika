import itertools

a = list(itertools.permutations("0123456789ABCDEF", r=3))
forbiddens = list(itertools.permutations('02468ACE', r=2)) + list(itertools.permutations('13579BDF', r=2))
counter = 0
for x in a:
    s1 = ''.join(x)
    if (s1[0]!='0'):
        for forbidden in forbiddens:
            s = ''.join(forbidden)
            if (s in s1):
                break
        else:
            counter += 1

print(counter)
