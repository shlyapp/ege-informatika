import itertools

a = list(itertools.permutations('0123456789', r = 6))
forbiddens = list(itertools.permutations('02468', r = 2)) + list(itertools.permutations('13579', r = 2))

counter = 0

for element in a:
    element = ''.join(element)
    if (element[0] != '0' and int(element) % 5 == 0):
        for forbidden in forbiddens:
            forbidden = ''.join(forbidden)
            if forbidden in element:
                break
        else:
            counter += 1

print(counter)
