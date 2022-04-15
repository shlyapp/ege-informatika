file = open('kompege/files/27B-2724.txt')
N = int(file.readline())
k = [0] * 131
counter = 0 

for i in range(N):
    num = int(file.readline())
    ost = 0 if num % 131 == 0 else 131 - num % 131
    counter += k[ost]

    k[num % 131] += 1

print(counter)