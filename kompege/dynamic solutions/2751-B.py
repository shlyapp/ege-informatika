file = open('kompege/files/27B-2751.txt')
N = int(file.readline())
buffer = [int(file.readline()) for i in range(4)]
k_13 = [0, 0]
k_0 = [0, 0]
counter = 0

for i in range(N - 4):
    num = int(file.readline())
    if num % 13 == 0:
        counter += k_0[1 - num % 2]
    else:
        counter += k_13[1 - num % 2]

    k_0[buffer[0] % 2] += 1
    if buffer[0] % 13 == 0:
        k_13[buffer[0] % 2] += 1

    buffer.append(num)
    buffer.pop(0)

print(counter)
