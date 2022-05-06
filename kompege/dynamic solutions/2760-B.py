file = open('kompege/files/27B-2760.txt')
N = int(file.readline())
data = [int(num) for num in file.readlines()]
minimum = float('inf')

for i in range(N):
    mass = data[i::5]
    if len(mass) == 1:
        continue
    k = [float('inf')] * 107
    for a in range(len(mass)):
        num = mass[a]
        ost = 0 if num % 107 == 0 else 107 - num % 107
        minimum = min(num + k[ost], minimum)

        k[num % 107] = min(k[num % 107], num)

print(minimum)
    
