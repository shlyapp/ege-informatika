file = open('kompege/files/27B-2756.txt')
N = int(file.readline())
m = [0] * 100
maximum = float('-inf')

for i in range(N):
    num = int(file.readline())
    ost = 12 - num % 12 if num % 100 <= 12 else 112 - num % 100
    if m[ost] > num and num + m[ost] > maximum:
        maximum = num + m[ost]

    m[num % 100] = max(m[num % 100], num)

print(maximum)