file = open('kompege/files/27B-2726.txt')
N = int(file.readline())
maximum = float('-inf')
k = [float('-inf')] * 2

for i in range(N):
    num = int(file.readline())
    # дополняющий остаток
    ost = 1 if num % 2 == 0 else 0
    maximum = max(maximum, k[ost] + num)

    k[num % 2] = max(k[num % 2], num)

print(maximum)