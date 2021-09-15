import itertools

a = list(itertools.product('ВИШНЯ', repeat=6))
forbiddens = ['И', 'Я']
counter = 0

for x in a:
    x = ''.join(x)
    if (x[0]!='Ш'):
        if (x.count('В') <= 1):
            for forbidden in forbiddens:
                forbidden = ''.join(forbidden)
                if (x[-1] == forbidden):
                    break
            else:
                counter +=1

print(counter)