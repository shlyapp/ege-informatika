with open('kpolyakov/Variants/18596/9.csv') as file:
    data = []
    for line in file.readlines():
        nums = list(map(int, line.split(';')))
        data.append(nums)

counter = 0

for line in data:
    a, b, c, d = line
    if (a + c == b + d):
        counter += 1

print(counter)
