file = open('kompege/files/27A-2759.txt')
N = int(file.readline())
data = [int(num) for num in file.readlines()]
counter = 0

for i in range(N):
    for j in range(i + 1, N):
        if data[i] > data[j] and data[i] + data[j] <= 134:
            counter += 1
        
print(counter)