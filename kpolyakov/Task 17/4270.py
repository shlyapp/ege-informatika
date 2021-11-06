file = open('kpolyakov/Task 17/17-1.txt')
data = []
for elem in file:
    data.append(int(elem[:-1]))

counter = 0
maximum = min(data)

for i in range(len(data) - 1):
    if (data[i] % 9 == 0 and data[i+1] % 9 != 0 and oct(data[i+1])[-1] == '3') or (data[i+1] % 9 == 0 and data[i] % 9 != 0 and oct(data[i])[-1] == '3'):
        counter += 1
        maximum = max(max(data[i], data[i+1]), maximum)

print(counter, maximum)