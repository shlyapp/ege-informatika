import math

with open('kpolyakov/Variants/43177/9.csv') as file:
    data = []
    for line in file.readlines():
        nums = list(map(int, line.split(';')))
        data.append(nums)


def calculate(point):
    return math.sqrt((-20 - point[0])**2 + (-20 - point[1])**2)


best = 0
for point in data:
    result = calculate(point)
    best = max(best, result)

print(best)
