file = open('kpolyakov/Task 17/17-1.txt')
data = list(map(int, file.readlines()[:-1]))

counter = 0
maximum = min(data)

for i in range(0, len(data) - 1):
    if (data[i - 1] > data[i] and data[i + 1] > data[i]):
        counter += 1
        maximum = max(maximum, data[i])

print(counter, maximum)