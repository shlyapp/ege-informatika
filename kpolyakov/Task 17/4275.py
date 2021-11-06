file = open('kpolyakov/Task 17/17-2.txt')
data = []
for num in file:
    data.append(int(num[:-1]))

counter = 0
max = max(data)

for element in data:
    if (element == max):
        counter += 1

for element in data:
    if (element == max):
        print(counter, data.index(element) + 1)
        break