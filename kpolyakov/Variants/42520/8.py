import itertools

a = list(itertools.product("МОИСЕЙ", repeat = 4))
vowel = ['О', 'И', 'Е']
counter = 0

for element in a:
    element = ''.join(element)
    if element[0] != 'Й':
        vowel_counter = sum([element.count(v) for v in vowel])
        if vowel_counter > 0:
            counter += 1

print(counter)
