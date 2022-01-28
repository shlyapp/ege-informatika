N =  10000
file = open('kpolyakov/Task 26/26-j8.txt')
data = sorted([int(x) for x in file])

sale1 = []
sale2 = []

for i in range(7000):
    sale1.append(data[i] * 0.3)

for i in range(7000, 10000):
    sale1.append(data[i] * 0.4)

for i in range(5000):
    sale2.append(data[i] * 0.4)

for i in range(5000, 10000):
    sale2.append(data[i] * 0.35)

print(int(sum(sale2)-sum(sale1)), max(data) - data[data.index(max(sale2))])