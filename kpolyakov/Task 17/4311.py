file = open('kpolyakov/Task 17/17-4.txt')
data = [int(x) for x in file]

summa = 0
maximum = min(data)

for element in data:
    if (element % 13 == 4) and (element % 8 == 1):
        summa += element
        maximum = max(maximum, element)

print(maximum, summa)