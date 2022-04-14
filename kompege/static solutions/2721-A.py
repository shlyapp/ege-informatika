import itertools

with open('kompege/files/27A-2721.txt') as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

counter = 0

for a, b in itertools.combinations(data, 2):
    if (a * b) % 65 == 0:
        counter += 1

print(counter)
