with open('kpolyakov/Task 27/27-50a.txt') as file:
    N = int(file.readline())
    data = []
    for i in range(N):
        a, b = (list(map(int, file.readline().split())))
        data.append([a, b, max(a, b), (a + b) % 2])

