file = open('kompege/files/27A-2754.txt')
N = int(file.readline())
data = [int(num) for num in file.readlines()]
maximum = float('-inf')

for i in range(N):
    for j in range(i + 1, N):
        if (j - i) >= 5 and (data[i] - data[j]) % 137 == 0:
            maximum = max(maximum, data[i] - data[j])

print(maximum)
