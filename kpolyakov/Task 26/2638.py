#1000 100
k = 100
file = open('kpolyakov/Task 26/26-k1.txt')
data = sorted([int(x) for x in file])[::-1]
summa = 0

for i in range(k):
    summa += data[i] * 0.2

print(data[k], summa)

