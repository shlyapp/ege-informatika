import itertools

with open('kompege/27A-2727.txt') as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

mininum = 1000000000

for couple in itertools.combinations(data, 2):
    if (couple[0] * couple[1]) % 31 == 0:
        mininum = min(mininum, (couple[0] * couple[1]))

print(mininum)
