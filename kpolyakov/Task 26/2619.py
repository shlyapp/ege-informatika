#47232 4497 

summa = 0
people = 0

file = open('kpolyakov/Task 26/26-2.txt')
data = sorted([int(x) for x in file])

for i in range(len(data)):
    if (summa + data[i] > 47232):
        people = i
        break
    summa += data[i]

ost = 47232 - (summa - data[people])
last = 0

for i in range(len(data)):
    if data[i] <= ost:
        last = max(last, data[i])

print(people, last)

