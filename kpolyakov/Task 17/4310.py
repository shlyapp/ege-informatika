from typing import Counter


file = open('kpolyakov/Task 17/17-4.txt')
data = [int(x) for x in file]

forbiddens = [7, 17, 19, 27]
counter = 0
maximum = -10000

for element in data:
    if (element % 3 == 0) and list(map(lambda x: str(element % x), forbiddens)).count('0') == 0:
        counter += 1
        maximum = max(maximum, element)

print(counter, maximum)