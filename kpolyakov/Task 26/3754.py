file = open("kpolyakov/Task 26/26-42.txt")
# 500 4000000
N = 4000000
data = []

for element in file:
    triple = [x for x in element.split()]
    triple[1] = int(triple[1]); triple[2] = int(triple[2])
    data.append(triple)

data = sorted(data)[::-1]
summa_Z = 0

for element in data:
    if element[0] == 'Z':
        summa_Z += element[1] * element[2]
    else:
        index = data.index(element)
        break

ost = N - summa_Z
data = sorted(data[index : N])
data2 = []

counter = 0

for element in data:
    # summa = element[1] * element[2]
    # if ost - summa > 0:
    #     counter += element[2]
    data2.append([element[2], element[1]])

data2 = sorted(data2)

for element in data2:
    print(element)

print(counter)