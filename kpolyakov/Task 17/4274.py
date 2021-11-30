file = open('kpolyakov/Task 17/17-1.txt')

data = []
for element in file:
    data.append(int(element))

counter = 0
maximum = min(data)

for i in range(1, len(data) - 1):
    if (data[i - 1] > data[i] and data[i + 1] > data[i]):
        counter += 1
        maximum = max(maximum, data[i])

print(counter, maximum)