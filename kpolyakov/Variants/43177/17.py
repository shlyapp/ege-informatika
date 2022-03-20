with open('kpolyakov/Variants/43177/17.txt') as file:
    data = [int(num) for num in file.readlines()]

minimum = min(data)
counter = 0
index = 0
for i in range(len(data)):
    if data[i] == minimum:
        counter += 1
        index = i + 1

print(counter, index)
