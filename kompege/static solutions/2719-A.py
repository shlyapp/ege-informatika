import itertools

with open('kompege/files/27A-2719.txt') as file:
    N = file.readline()
    data = (int(num) for num in file.readlines())

counter = 0

for a, b in itertools.combinations(data, 2):
    if (a + b) % 2 == 0:
        counter += 1

print(counter)
