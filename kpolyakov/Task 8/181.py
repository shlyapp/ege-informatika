import itertools

a = list(itertools.permutations("ЗАПИСЬ", r=6))
counter = 0
f = ['АЬ', 'ИЬ']
for x in a:
    if (x[0]!='Ь'):
        s = ''.join(x)
        for forbidden in f:
            if forbidden in s:
                break
        else:
            counter += 1

print(counter)