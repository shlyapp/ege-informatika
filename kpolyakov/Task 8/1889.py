import itertools

a = list(itertools.permutations('ВУАЛЬ', r=5))
forbiddens = ['ЬА', 'ЬУ']
counter = 0

for x in a:
    s1 = ''.join(x)
    if (s1[0]!='Ь'):
        for forbidden in forbiddens:
            s = ''.join(forbidden)
            if (s in s1):
                break
        else:
            counter += 1

print(counter)