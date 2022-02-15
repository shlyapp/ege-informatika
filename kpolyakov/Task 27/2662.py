with open('kpolyakov/Task 27/27-2b.txt') as file:
    N = int(file.readline())
    data = []
    for i in range(N):
        a, b = map(int, file.readline().split())
        data.append([a, b, abs(a - b)])

data.sort(key = lambda x: x[2])

summa = sum([max(i[0], i[1]) for i in data])

for i in range(N):
    if summa % 3 != 0:
        print(summa)
        break
    summa -= data[i][2]


