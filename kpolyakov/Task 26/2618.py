#34252 3284 

summa = 0
people = 0

file = open('kpolyakov/Task 26/26-1.txt')
data = sorted([int(x) for x in file])

for i in range(len(data)):
    if (summa + data[i] > 34252):
        people = i
        break
    summa += data[i]

ost = 34252 - (summa - data[people])
last = 0

# for i in range(len(data)):
#     if data[i] < ost:
#         last = max(last, data[i])
#     else:
#         break

last = max((data[i] for i in range(len(data)) if data[i] < ost))

print(people, last)

