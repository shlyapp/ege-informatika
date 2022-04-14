import itertools

with open('kompege/files/27A-2732.txt') as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

maximum = 0

for a, b in itertools.combinations(data, 2):
    if abs(a - b) % 80 == 0:
        maximum = max(maximum, abs(a - b))

print(maximum)
