file = open('kompege/files/27B-2754.txt')
N = int(file.readline())
m = [float('-inf')] * 137
buffer = [int(file.readline()) for i in range(4)]
maximum = float('-inf')

for i in range(N - 4):
    num = int(file.readline())
    maximum = max(maximum, m[num % 137] - num)

    m[buffer[0] % 137] = max(m[buffer[0] % 137], buffer[0])
    buffer.append(num)
    buffer.pop(0)

print(maximum)
