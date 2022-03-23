with open('kpolyakov/Variants/18596/17.txt') as file:
    data = [int(num) for num in file.readlines()]

counter = 0
maximum = 0

for i in range(len(data) - 3):
    nums = [data[i], data[i + 1], data[i + 2], data[i + 3]]
    delim = list(map(lambda x: str(x % 2), nums))
    delim = ''.join(delim)
    if '00' not in delim and '11' not in delim:
        counter += 1
        maximum = max(maximum, sum(nums))

print(counter, maximum)
