import itertools

with open('kompege/27A-2720.txt') as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

counter = 0

for a, b in itertools.combinations(data, 2):
    if (a * b) % 7 == 0:
        counter += 1

print(counter)
