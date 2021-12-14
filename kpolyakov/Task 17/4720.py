file = open("kpolyakov/Task 17/17-243.txt")
data = [int(x) for x in file]

summa = 0
counter = 0
minimum = 10000

summa = sum(sum(map(int, str(element))) for element in data if element % 49 == 0)

for i in range(len(data) - 1):
    if (data[i] > summa and data[i + 1] <= summa and data[i + 1] % 10 == 7) or (data[i + 1] > summa and data[i] <= summa and data[i] % 10 == 7):
        counter += 1
        minimum = min(minimum, data[i] + data[i + 1])

print(counter, minimum)