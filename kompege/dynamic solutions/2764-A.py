file = open('kompege/files/27A-2764.txt')
N = int(file.readline())
data = [int(num) for num in file.readlines()]
minimum = float('inf')

for i in range(N):
    for j in range(i + 1, N):
        if j - i >= 7 and (data[i] + data[j])  % 23 == 0 and (data[i] * data[j]) % 6 == 0:
            minimum = min(minimum, data[i] + data[j])
    
print(minimum)