file = open('kompege/files/27B-2727.txt')
N = int(file.readline())
# предыдущие минимальные числа
k = [float('inf'), float('inf')]
minimum = float('inf')

for i in range(N):
    num = int(file.readline())
    if num % 2 == 0:
        minimum = min((k[0] * num, k[1] * num, minimum))
    else:
        minimum = min((k[0] * num, minimum))

    if num % 2 == 0:
        k[0] = min(k[0], num)
    else:
        k[1] = min(k[1], num)

print(minimum)
# 21831874