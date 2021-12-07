file = open("kpolyakov/Task 17/17-8.txt")
data = [int(x) for x in file]

counter = 0
maximum = 0

for i in range(len(data) - 1):
    if any(map(lambda x: bin(x)[2:].count('1') > 5 and bin(x)[2:].count('1') % 2 != 0, [data[i], data[i +1]])):
        counter += 1
        maximum = max(maximum, data[i] + data[i + 1])

print(counter, maximum)