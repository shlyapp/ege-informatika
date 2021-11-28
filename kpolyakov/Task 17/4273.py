file = open('kpolyakov/Task 17/17-1.txt')
data = list(map(int, file.readlines()[:-1]))

counter = 0
last_index = 0
min_length = 100000

for i in range(1, len(data) - 1):
    if (data[i - 1] < data[i] and data[i + 1] < data[i]):
        counter += 1
        if (last_index != 0):
            min_length = min(min_length, (i - last_index))
            last_index = i
        else:
            last_index = i


print(counter, min_length)