file = open('kpolyakov/Task 27/27A-2672.txt')
N = int(file.readline())
data = [int(num) for num in file.readlines()]
counter = 0 

for i in range(N):
    for j in range(i + 1, N):
        if (data[i] * data[j]) % 6 == 0:
            counter += 1

print(counter)