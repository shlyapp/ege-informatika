with open('dosrok/26.txt') as file:
    N = int(file.readline())
    data = [list(map(int, num.split())) for num in file.readlines()]

def sort_by_first_value(value):
    return value[0], - value[1]

K = 11

data.sort(key = sort_by_first_value)

for i in range(N - 1):
    if data[i][0] ==  data[i + 1][0]:
        if data[i][1] - data[i + 1][1] - 1 == K:
            value = data[i + 1]
            print(value[0], value[1] + 1)
