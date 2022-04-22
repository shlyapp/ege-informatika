file = open('kompege/files/27A-2753.txt')
N = int(file.readline())
data = [int(num) for num in file]
counter = 0

for i in range(N):
    for j in range(i + 1, N):
        if (j - i) <= 7 and (data[i] + data[i]) % 8 != 0:
            counter += 1

print(counter)