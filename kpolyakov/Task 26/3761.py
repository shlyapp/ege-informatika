N =  5000
file = open('kpolyakov/Task 26/26-45.txt')
data = [int(num) for num in file]

a = []

for i in range(0, N - 1):
    for j in range(i + 1, N):
        if (data[i] + data[j]) % 2 == 0:
            a.append((data[i] + data[j]) // 2)


b = set(a)
counter = 0

for element in data:
    if element in b:
        counter += a.count(element)

print(counter)
