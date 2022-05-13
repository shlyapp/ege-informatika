file = open('kpolyakov/Task 27/27B-2676.txt')
N = int(file.readline())
# fisrt % 2, second % 13
k = [[0] * 2 for i in range(2)]
counter = 0

for i in range(N):
    num = int(file.readline())
    if num % 13 == 0:
        counter += k[not(bool(num % 2))][1]
    counter += k[not(bool(num % 2))][0]

    k[num % 2][bool(num % 13)] += 1

print(counter)