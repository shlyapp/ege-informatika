def sort_by_alphabet(str):
    return str[0]

def sort_by_length(str):
    return len(str)

data = ['a', 'cc', 'bbb']
print(data)

data.sort()
print(f'Стандартная сортировка: {data}')
data.sort(key = sort_by_alphabet)
print(f'Сортировка по алфавиту: {data}')
data.sort(key = sort_by_length)
print(f'Сортировка по длине: {data}')
data.sort(key = sort_by_length, reverse = True)
print(f'Сортировка по уменьшению длины: {data}')

data = [['A', 1, 2], ['B', 2, 1]]
print(data)

def sort_by_first_num(str):
    return str[1]

def sort_by_second_num(str):
    return str[2]

def sort_by_model(str):
    return str[0]

data.sort(key = sort_by_first_num)
print(data)

data.sort(key = sort_by_second_num)
print(data)

data.sort(key = sort_by_model)
print(data)

data = [['A', 10], ['A', 5], ['A', 12], ['Z', 1]]

def sort_by_model_and_num(str):
    return str[0], str[1]

data.sort(key = sort_by_model_and_num)
print(data)