import itertools

with open('kompege/files/27A-2729.txt') as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

minimum = 1000000000

for threes in itertools.combinations(data, 3):
    if sum(threes) % 11 == 0:
        minimum = min(minimum, sum(threes))

print(minimum)
