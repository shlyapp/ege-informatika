file = open('kpolyakov/Task 17/17-1.txt')
data = list(map(int, file.readlines()[:-1]))

counter = 0
maximum = min(data)

for i in range(1, len(data) - 2):
    if (data[i - 1] > data[i] and data[i + 1] > data[i]):
        counter += 1
        maximum = max(maximum, data[i])

if (data[0] < data[1]):
    counter += 1
if (data[-2] < data[-1]):
    counter += 1

print(counter, maximum)