file = open('kpolyakov/Task 26/26-j3.txt')
data = sorted([int(x) for x in file])[::-1]
N = 1000000
summa = 0
people = 0

for i in range(len(data)):
    if (summa + data[i] > N):
        people = i
        break
    summa += data[i]

print(people + 1, N - summa)