file = open('kpolyakov/Variants/44140/27A.txt')
N = int(file.readline())
data = [int(num) for num in file.readlines()]
counter = 0

for i in range(N):
    for j in range(i + 1, N):
        if j - i >= 7 and (data[i] * data[j]) % 14 == 0:
            counter += 1

print(counter)
