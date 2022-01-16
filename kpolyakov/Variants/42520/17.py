file = open('kpolyakov/Task 17/17-1.txt')
data = list(map(int, file.readlines()[:-1]))

arithmetic_mean = sum(data) / len(data)
counter = 0
maximum = 0 

for i in range(len(data) - 1):
    if (data[i] < arithmetic_mean or data[i + 1] < arithmetic_mean) and (str(data[i])[-2:] == '13' or str(data[i + 1])[-2:] == '13'):
        counter += 1
        maximum = max(maximum, data[i] + data[i + 1])

print(counter, maximum)