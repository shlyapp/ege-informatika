with open('kompege/27B-2738.txt') as file:
    N = int(file.readline())
    data = [int(num) for num in file.readlines()]

nums = []

for element in data:
    for num in str(element):
        nums += [num]

answer = list(map(lambda x: [x, nums.count(x)], set(nums)))
answer.sort(key=lambda x: x[1])
print(answer[0][1])
