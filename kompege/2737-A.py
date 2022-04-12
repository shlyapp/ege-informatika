import itertools

with open('kompege/27A-2737.txt') as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

counter = 0

for couple in itertools.combinations(data, 2):
    if sum(couple) == 2000:
        counter += 1

print(counter)
