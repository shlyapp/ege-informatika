file = open('kompege/files/27B-2727.txt')
N = int(file.readline())
k = [float('inf'), float('inf')]
minimum = float('inf')

for i in range(N):
    num = int(file.readline())

    if num % 31 == 0:
        minimum = min(k[1] * num, minimum)
    minimum = min((k[0] * num, minimum))

    index = 0 if num % 31 == 0 else 1
    k[index] = min(k[index], num)

print(minimum)
