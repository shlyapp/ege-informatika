file = open('kompege/files/27B-2760.txt')
N = int(file.readline())
k = [[0] * 13 for i in range(2)]
buffer = [int(file.readline()) for i in range(5)]
counter = 0

for i in range(N - 5):
    num = int(file.readline())
    if num % 2 == 0:
        counter += k[0][num % 13] + k[1][num % 13]
    else:
        counter += k[0][num % 13]

    k[buffer[0] % 2][buffer[0] % 13] += 1
    buffer.append(num)
    buffer.pop(0)

print(counter)
