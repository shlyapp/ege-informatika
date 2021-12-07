file = open('kpolyakov/Task 17/17-3.txt')
data = [int(x) for x in file]

counter = 0
maximum = -10000

for i in range(len(data) - 1):
    if ((data[i] % 2 == 0 and abs(data[i]) % 4 == 0) and (data[i + 1] % 2 != 0 and abs(data[i + 1] % 11 == 0))) or ((data[i + 1] % 2 == 0 and abs(data[i + 1]) % 4 == 0) and (data[i] % 2 != 0 and abs(data[i] % 11 == 0))):
        counter += 1
        maximum = max(maximum, data[i] + data[i + 1])

print(counter, maximum)
