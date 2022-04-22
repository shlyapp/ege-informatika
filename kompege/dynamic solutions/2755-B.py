file = open('kompege/files/27B-2755.txt')
N = int(file.readline())
minimum = float('inf')
m = [float('inf')] * 144

for i in range(N):
    num = int(file.readline())
    ost = 0 if num % 144 == 0 else 144 - num % 144

    if m[ost] < num:
        minimum = min(minimum, num + m[ost])

    m[num % 144] = min(num, m[num % 144])

print(minimum)
