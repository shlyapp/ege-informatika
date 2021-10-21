def F(n):
    n = list(map(int, str(n)))
    nums = [n[0] + n[1], n[1] + n[2], n[2] + n[3]]
    nums.sort()
    nums.remove(nums[0])
    return str(nums[0]) + str(nums[1])

for i in range(1000, 9999):
    if (F(i) == '613'):
        print(i)