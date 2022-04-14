import itertools

with open("kompege/files/27A-2724.txt") as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

counter = 0

for couple in itertools.combinations(data, 2):
    if sum(couple) % 131 == 0:
        counter += 1

print(counter)
