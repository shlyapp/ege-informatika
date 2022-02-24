with open('kpolyakov/Task 27/27-14a.txt') as file:
    N = int(file.readline())
    data = [int(file.readline()) for i in range(N)]

delim = [0 for i in range(12)]

# for element in range(N - 1):
#     delim[element % 12] += 1

from itertools import  *

for i, j in combinations(data, 2):
    print(i, j)

counter = 0

for i in range(7):
    if i == 0 or i == 6: counter += (delim[i]*(delim[i] - 1)) / 2
    else:
        counter += delim[12 - i] * delim[i]

print(counter)

