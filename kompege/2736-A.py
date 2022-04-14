from collections import Counter

with open("kompege/27A-2736.txt") as file:
    data = [int(num) for num in file.readlines()]

nums = []

for element in data:
    nums += [str(element)[0]]

nums = Counter(nums)
print(nums.most_common()[-1][1])
