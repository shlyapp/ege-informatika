with open('kompege/files/27B-2737.txt') as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

k = [0] * 2000

for element in data:
    if element <= 2000:
        k[2000 - element] += 1

counter = k[0]*(k[0] - 1) // 2 + k[1000]*(k[1000] - 1) // 2

for i in range(1, 1000):
    counter += k[i] * k[-i]

print(counter)
