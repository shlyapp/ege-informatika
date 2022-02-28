with open('kpolyakov/Task 27/27-72b.txt') as file:
    N = int(file.readline())
    counter = 0
    k = [0] * 71
    s = 0
    for i in range(N):
        x = int(file.readline())
        s += x
        if s % 71 == 0:
            counter += 1
        counter += k[s % 71]
        k[s % 71] += 1

print(counter)
