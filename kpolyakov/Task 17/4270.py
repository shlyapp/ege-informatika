file = open('kpolyakov/Task 17/17-1.txt')
data = []
for elem in file:
    data.append(int(elem[:-1]))

counter = 0
minimum = max(data)

for i in range(len(data) - 1):
    if (str(data[i])[-1] == '6' and data[i] % 3 == 0) or (str(data[i + 1])[-1] == '6' and data[i+1] % 3 == 0):
        counter += 1
        if (data[i] < minimum):
            minimum = data[i]
        if (data[i + 1] < minimum):
            minimum = data[i + 1]

print(counter, minimum)