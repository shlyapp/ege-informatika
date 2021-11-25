file = open('kpolyakov/Task 17/17-1.txt')
data = list(map(int, file.readlines()[:-1]))
maximum = 0
counter = 1

for i in range(1, len(data)):
    if (data[i] < data[i-1]):
        counter += 1
    else:
        maximum = max(maximum, counter)
        counter = 1

maximums = 0

for i in range(1, len(data)):
    if (data[i] < data[i-1]):
        counter += 1
    else:
        if (counter == maximum): maximums += 1
        counter = 1

print(maximum, maximums)