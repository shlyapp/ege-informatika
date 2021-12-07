file = open('kpolyakov/Task 17/17-4.txt')
data = [int(x) for x in file]

counter = 0
maximum = min(data)
minimum = max(data)
forbiddens = [2, 3, 5, 7]

for element in data:
    if (list(map(lambda x: str(element % x), forbiddens))).count('0') == 2:
        counter += 1
        minimum = min(minimum, element)
        maximum = max(maximum, element)

print(counter, minimum + maximum)