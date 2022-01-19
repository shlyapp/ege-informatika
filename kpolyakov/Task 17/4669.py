file = open("kpolyakov/Task 17/17-4.txt")
data = [int(x) for x in file]

sr = sum(data) / len(data)
minimum = 20000
counter = 0

for i in range(len(data) - 1):
    if (data[i] < sr or data[i + 1] < sr) and (str(data[i]).count('5') == 0 or str(data[i + 1]).count('5') == 0):
        counter += 1
        minimum = min(minimum, data[i] + data[i + 1])

print(counter, minimum)
