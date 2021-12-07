file = open('kpolyakov/Task 17/17-4.txt')
data = [int(x) for x in file]

counter = 0
summa = 0

for element in data:
    if (element % 3 == 0 and element % 9 != 0) and (element % 10 >= 4):
        counter += 1
        summa += element

print(counter, int(summa / counter))