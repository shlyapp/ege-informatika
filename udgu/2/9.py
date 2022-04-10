with open('udgu/2/9.csv') as file:
    counter = 0
    for line in file.readlines():
        nums = list(map(int, line.split(';')))
        if sum(nums) == 180 and (nums[0] == 90, nums[1] == 90, nums[2] == 90).count(1) == 1:
            counter += 1

print(counter)
