#9954
file = open('kpolyakov/Task 26/26-j5.txt')
data = [int(x) for x in file]
data2 = [0 for i in range(len(data))]

for i in range(1, len(data)-1):
    data2[i] = sorted([data[i-1], data[i], data[i + 1]])[1]

counter = 0
for i in range(1, len(data)-1):
    counter += data2[i]-data[i]

print(counter)

# сделать тестовый код для примера
# из задачи, а потом уже брать весь
# массив данных