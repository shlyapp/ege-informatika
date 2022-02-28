
with open('kpolyakov/Task 27/27-14b.txt') as file:
    N = int(file.readline())
    data = [int(file.readline()) for i in range(N)]

div = [0 for i in range(12)]

for num in data:
    div[num % 12] += 1

counter = 0

for i in range(7):
    if i == 6 or i == 0:
        counter += div[i] * (div[i] - 1) / 2
    else:
        counter += div[i] * div[12 - i]

print(int(counter))
