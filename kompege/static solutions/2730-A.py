import itertools

with open('kompege/files/27A-2730.txt') as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

maximum = 0

for a, b, c, d in itertools.combinations(data, 4):
    if (a * b * c * d) % 12 == 0:
        maximum = max(maximum, a + b + c + d)

print(maximum)
