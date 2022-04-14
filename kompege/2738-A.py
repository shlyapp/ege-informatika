from collections import Counter

with open('kompege/27A-2738.txt') as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

nums = []

for element in data:
    for num in str(element):
        nums += [num]

nums = Counter(nums)

print(nums.most_common()[-1][1])
