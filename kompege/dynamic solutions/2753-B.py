file = open('kompege/files/27B-2753.txt')
N = int(file.readline())
data = [int(num) for num in file.readlines()]
counter = 0

for i in range(N):
    for j in range(i + 1, N):
        if (j - i) > 7:
            break
        if (data[i] + data[j]) % 8 != 0:
            counter += 1

print(counter)
