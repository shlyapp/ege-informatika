file = open('kpolyakov/Task 17/17-3.txt')
data = [int(x) for x in file]

counter = 0
maximum = -100000

for i in range(len(data) - 1):
    if abs(data[i] + data[i + 1]) % 3 == 0 and abs(data[i] + data[i + 1]) % 6 !=0 and abs(data[i] * data[i + 1]) % 10 == 8:
        counter += 1
        maximum = max(data[i] + data[i + 1], maximum)

print(counter, maximum)
