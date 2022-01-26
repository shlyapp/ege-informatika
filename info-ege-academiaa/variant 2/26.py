#13820 1325 

N = 13820

file = open("info-ege-academiaa/variant 2/26.txt")
data = sorted([int(x) for x in file])

summa = 0
elements = []

for i in range(len(data)):
    if data[i] + summa > N:
        people = i
        break
    summa += data[i]
    elements.append(data[i])

ost = N - (summa - data[people])

print(people, ost)

