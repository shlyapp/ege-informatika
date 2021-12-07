file = open('kpolyakov/Task 17/17-3.txt')
data = [int(x) for x in file]

counter = 0
maximum = -10000

for i in range(len(data) - 1):
    if abs(data[i] + data[i + 1]) % 2 == 0 and abs(data[i] + data[i + 1]) % 10 != 6:
        counter += 1
        maximum = max(maximum, (data[i] + data[i + 1]) // 2)

print(counter, maximum)