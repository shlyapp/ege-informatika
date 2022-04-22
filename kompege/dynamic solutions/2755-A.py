file = open('kompege/files/27A-2755.txt')
N = int(file.readline())
data = [int(num) for num in file.readlines()]
minimum = float('inf')

for i in range(N):
    for j in range(i + 1, N):
        if data[i] < data[j] and (data[i] + data[j]) % 144 == 0:
            minimum = min(minimum, data[i] + data[j])

print(minimum)
