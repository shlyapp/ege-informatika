file = open('kpolyakov/Task 17/17-4.txt')
data = [int(x) for x in file]

counter = 0
maximum = min(data)
minimum = max(data)

for element in data:
    if (element % 10 == 5 or element % 10 == 7) and (element % 9 != 0 and element % 11 != 0):
        counter += 1
        maximum = max(maximum, element)
        minimum = min(minimum, element)

print(counter, maximum + minimum)