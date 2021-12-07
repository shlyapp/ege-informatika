file = open('kpolyakov/Task 17/17-4.txt')
data = [int(x) for x in file]

counter = 0
minimum = max(data)

for element in data:
    if (element % 100 // 10 <= 4) and (3 <= element % 1000 // 100 <= 7):
        counter += 1
        minimum = min(minimum, element)

print(counter, minimum)
