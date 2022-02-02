file = open('kpolyakov/Task 26/26-46.txt')
N = 500
data = [int(x) for x in file]

minimum = 10000000000000000
a = []

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            element = data[i] + data[j] + data[k]
            if element % 3 == 0:
                a.append(element // 3)

b = set(a)
counter = 0

for element in data:
    if element in b:
        counter += a.count(element)
        minimum = min(minimum, element)

print(counter, minimum)