with open('kompege/files/27B-2725.txt') as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

counter = 0
k = [0] * 69

for element in data:
    k[element % 69] += 1

for i in range(69):
    counter += k[i]*(k[i] - 1) // 2

print(counter)
