# s = 'АБВГД БЕВ ВЕЖЗ ГВЗ ДГЗ ЕИЖ ЖИ ЗЖИ ИКЛ КМ ЛМ М'
# d = {i[0]:i[1:] for i in s.split()}
# find = lambda a, b: (a == b) + sum(find(c, b) for c in d[a])
# print(find(*'АМ'))

s = 'АБГД БВГ ВИЕ ГВЕЖ ДГЖ ЕИМК ЖЕК ИМ КМ М'
d = {i[0]:i[1:] for i in s.split()}

def find(a, b):
    if a == b: return 1
    counter = 0 
    for c in d[a]:
        counter += find(c, b)
    return counter

print(find(*'АВ') * find(*'ВМ'))