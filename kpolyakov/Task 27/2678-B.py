file = open('kpolyakov/Task 27/27B-2678.txt')
N = int(file.readline())
data = [int(num) for num in file.readlines()]
counter = 0

for i in range(N):
    for j in range(i + 1, N):
        if j - i >= 5:
            break
        if (data[i] * data[j]) % 13 == 0 and (data[i] + data[j]) % 2 != 0:
            counter += 1
        

print(counter)