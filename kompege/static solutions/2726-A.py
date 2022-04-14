import itertools

with open('kompege/files/27A-2726.txt') as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

maximum = 0

for couple in itertools.combinations(data, 2):
    if sum(couple) % 2 != 0:
        maximum = max(maximum, sum(couple))

print(maximum)
