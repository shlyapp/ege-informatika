import itertools

a = list(itertools.product("ABCDE", repeat = 4))
forbiddens = ['BA', 'BE', 'CA', 'CE', 'DA', 'DE', 'BC', 'BD', 'CD', 'EA']
counter = 0

for element in a:
    element = ''.join(element)
    for forbidden in forbiddens:
        forbidden = ''.join(forbidden)
        if forbidden in element:
            break
    else:
        counter += 1

print(counter)