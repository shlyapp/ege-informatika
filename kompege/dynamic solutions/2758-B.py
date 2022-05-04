file = open('kompege/files/27B-2758.txt')
N = int(file.readline())
data = [int(num) for num in file.readlines()]
minimum = float('inf')

for i in range(N):
    for j in range(i +  1, N):
        if j - i > 12:
            break
        s = data[i] + data[j]
        if s % 2 == 0 and s % 1071 == 0:
            minimum = min(minimum, s)

print(minimum)
    