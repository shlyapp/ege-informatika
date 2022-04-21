file = open('kompege/files/27B-2757.txt')
N = int(file.readline())
buffer = [int(file.readline()) for i in range(8)]
k_23 = 0
counter = 0

for i in range(N - 8):
    num = int(file.readline())
    if num % 23 == 0:
        counter += i
    else:
        counter += k_23

    if buffer[0] % 23 == 0:
        k_23 += 1

    buffer.append(num)
    buffer.pop(0)

print(counter)
