def counter_div(num):
    return len([x for x in range(2, num) if num % x == 0])

nums = []
for i in range(1000000, 1300001):
    if all(map(lambda x: int(x) < 3, str(i))) and sum(map(int, str(i))) % 10 == 0:
        nums.append(i)

for i in range(10, len(nums) + 1, 10):
    print(nums[i - 1], counter_div(nums[i - 1]))