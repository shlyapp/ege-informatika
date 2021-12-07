file = open('kpolyakov/Task 17/17-4.txt')
data = [int(x) for x in file]

counter = 0
summa = 0

for element in data:
    if (element % 16 == 11 and element % 7 == 0) and (element % 6 != 0 and element % 13 != 0 and element % 19 != 0):
        counter += 1
        summa += element

print(summa, counter)