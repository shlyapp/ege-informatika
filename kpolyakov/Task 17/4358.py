file = open("kpolyakov/Task 17/17-7.txt")
data = [int(x) for x in file]

counter = 0
maximum = min(data)

for element in data:
    if (element % 16 == 9) and (element % 16 // 16 % 16 != 10):
        counter += 1
        maximum = max(maximum, element)

print(counter, maximum)