import itertools

with open('kompege/27A-2728.txt') as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

maximum = 0

for couple in itertools.combinations(data, 2):
    if sum(couple) % 2 == 0 and sum(map(lambda x: x % 23 == 0, couple)) > 0:
        maximum = max(maximum, sum(couple))

print(maximum)
