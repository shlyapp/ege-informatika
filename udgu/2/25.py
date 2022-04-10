with open('udgu/2/A.txt') as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

counter = 0

for i in range(N):
    for j in range(i + 1, N):
        if (data[i] + data[j]) % 2 == 0 and data[i:j+1].count(0) > 0:
            counter += 1
            print(data[i:j+1])

print(counter)
