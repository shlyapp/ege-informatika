file = open('kompege/files/27B-2764.txt')
N = int(file.readline())
buffer = [int(file.readline()) for i in range(6)]
minimum = float('inf')
m = [[float('inf')] * 23, [float('inf')] * 23]

for i in range(N - 6):
    num = int(file.readline())
    # update maximum
    ost = 0 if num % 23 == 0 else 23 - num % 23
    if num % 6 == 0:
        minimum = min(m[1][ost] + num, minimum)
    minimum = min(m[0][ost] + num, minimum)  

    # update statictics
    next = buffer[0]  
    m[0 if next % 6 == 0 else 1][next % 23] = min(m[0 if next % 6 == 0 else 1][next % 23], next)

    buffer.append(num)
    buffer.pop(0)

print(minimum)