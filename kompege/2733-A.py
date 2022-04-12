import itertools

with open('kompege/27A-2733.txt') as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

counter = 0

for couple in itertools.combinations(data, 2):
    if sum(couple) % 80 == 0 and sum(map(lambda x: x > 50000, couple)) > 0:
        counter += 1

print(counter)
