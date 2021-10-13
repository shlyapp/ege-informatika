import itertools

def F(a):
    a = list((itertools.permutations(a, r=2)))
    max = 0
    min = 1000
    for element in a:
        stroka = ''.join(element)
        if stroka[0] == '0':
            a[a.index(element)] = (stroka[1], stroka[0])
    for element in a:
        element = ''.join(element)
        if int(element) > max:
            max = int(element)
        if int(element) < min:
            min = int(element)
    return max-min

for i in range(100, 1000):
    num = str(i)
    if (F(num) == 14):
        print(i)