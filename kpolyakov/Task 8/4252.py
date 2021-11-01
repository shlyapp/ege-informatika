import itertools

a = set(itertools.permutations('ОДЕКОЛОН', r = 8))
counter = 0

for element in a:
    element = ''.join(element)
    for i in range(len(element) - 1):
        if (element[i] == element[i + 1]):
            break
    else:
        counter += 1

print(counter)