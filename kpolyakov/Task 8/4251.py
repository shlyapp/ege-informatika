import itertools

a = set(itertools.permutations("ЗЕРККККАЛО", r = 6))
counter = 0

for element in a:
    element = ''.join(element)
    if (element.count('К') > 0):
        counter += 1

print(counter)