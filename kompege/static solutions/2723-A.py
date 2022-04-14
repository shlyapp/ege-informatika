import itertools

with open('kompege/files/27A-2723.txt') as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

counter = 0

for trinity in itertools.combinations(data, 3):
    if all(map(lambda x: x % 19 == 0, trinity)):
        counter += 1

print(counter)
