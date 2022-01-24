file = open('kpolyakov/Task 26/26-j5.txt')
data1 = [int(x) for x in file]
data2 = [data1[i] for i in range(len(data1))]

for i in range(len(data1)-2):
    data2[i + 1] = sorted(data1[i:i+3])[1]

summa = 0

minim = min(data2)

for i in range(len(data1)):
   if data1[i] > data2[i]:
       summa += data1[i] - data2[i]

print(data2[1:-1].count(minim), summa)
