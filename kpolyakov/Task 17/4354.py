file = open('kpolyakov/Task 17/17-6.txt')
data = [int(x) for x in file]

counter = 0
summa = 0

for i in range(len(data) // 3 * 3):
    if all((map(lambda x: bin(data[x])[2:].count('1') == 3, [x for x in range(i, i + 3)]))):
        counter += 1
        summa += max([data[x] for x in range(i, i + 3)])

print(counter, summa)


