file = open('kompege/files/27A-2756.txt')
N = int(file.readline())
data = [int(num) for num in file.readlines()]
maximum = float('-inf')

for i in range(N):
    for j in range(i + 1, N):
        if data[i] > data[j] and (data[i] + data[j]) % 100 == 12:
            maximum = max(maximum, data[i] + data[j])

print(maximum)

