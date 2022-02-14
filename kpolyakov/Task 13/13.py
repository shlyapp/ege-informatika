points = "АБВГД БЕВ ВЕЖЗ ГВЗ ДГЗ ЕИЖ ЖИ ЗЖИ ИКЛ КМ ЛМ М".split()
dict = {p[0]:p[1:] for p in points}

def find(start, end):
    if start == end: return 1
    counter = 0
    for d in dict[start]:
        counter += find(d, end)
    return counter 

print(find('А', 'М'))

# аналогичное решение однострочником

points = "АБВГД БЕВ ВЕЖЗ ГВЗ ДГЗ ЕИЖ ЖИ ЗЖИ ИКЛ КМ ЛМ М".split()
dict = {p[0]:p[1:] for p in points}
find = lambda start, end: (start == end) + sum(find(d, end) for d in dict[start])
print(find('А', 'М'))