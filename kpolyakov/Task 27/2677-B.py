file = open('kpolyakov/Task 27/27A-2677.txt')
N = int(file.readline())
counter = 0
k = [[0] * 2 for i in range(2)]
buffer = [int(file.readline()) for i in range(4)]

for i in range(N - 4):
    num = int(file.readline())
    if num % 13 == 0:
        counter += k[1 - num % 2][1]
    counter += k[1 - num % 2][0]

    next = buffer[0]
    k[next % 2][0 if num % 13 == 0 else 1] += 1
    buffer.append(num)
    buffer.pop(0)

print(counter)
