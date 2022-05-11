file = open('kpolyakov/Variants/44140/27B.txt')
N = int(file.readline())
k = [0] * 14
buffer = [int(file.readline()) for i in range(6)]
counter = 0

for i in range(N - 6):
    num = int(file.readline())
    for j in range(14):
        if (num * j) % 14 == 0:
            counter += k[j]

    k[buffer[0] % 14] += 1
    buffer.append(num)
    buffer.pop(0)

print(counter)
