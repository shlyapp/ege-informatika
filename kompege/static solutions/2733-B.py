with open('kompege/files/27B-2733.txt') as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

k_0 = [0] * 80
k_1 = [0] * 80

for element in data:
    if element > 50000:
        k_1[element % 80] += 1
    else:
        k_0[element % 80] += 1

counter = (k_1[0]*(k_1[0] - 1) // 2) + (k_1[40]*(k_1[40] - 1) // 2)
for i in range(1, 40):
    counter += k_1[i] * k_1[-i]

counter += (k_1[0] * k_0[0]) + (k_1[40] * k_0[40])
for i in range(1, 40):
    counter += k_0[i] * k_1[-i]
    counter += k_1[i] * k_0[-i]

print(counter)
