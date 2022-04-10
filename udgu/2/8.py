import itertools

a = list(itertools.product('МЕТРО', repeat=4))

counter = 0

for element in a:
    element = ''.join(element)
    if element[0] in 'МТР' and element[-1] in 'ЕО':
        counter += 1

print(counter)
