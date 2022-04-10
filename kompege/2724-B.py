with open("kompege/27B-2724.txt") as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

k = [0] * 131

for element in data:
    k[element % 131] += 1

counter = k[0] * (k[0] - 1) // 2

for i in range(1, len(k) // 2 + 1):
    counter += k[i]*k[-i]

print(counter)
